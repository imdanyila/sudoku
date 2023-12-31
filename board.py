import cell
import sudokuGenerator
import pygame
import sudoku
import copy


class Board:
    # initializes board
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.cells = [[], [], [], [], [], [], [], [], []]
        self.selected_cell = None
        if difficulty == 0:
            removed = 30
        elif difficulty == 1:
            removed = 40
        elif difficulty == 2:
            removed = 50
        # runs sudoku_generator to generate a sudoku problem
        self.original_board = sudokuGenerator.generate_sudoku(9, removed)
        self.sudoku = copy.deepcopy(self.original_board)
        # generates associated cell objects
        for row in range(0, 9):
            for col in range(0, 9):
                self.cells[row].append(cell.Cell(self.sudoku[row][col], row, col, self.screen))

        self.lives = 3  # Initialize with the maximum number of lives
        self.heart_images = [
            pygame.image.load('images/0.png'),
            pygame.image.load('images/1.png'),
            pygame.image.load('images/2.png'),
            pygame.image.load('images/3.png')
        ]

    # draws board to screen
    def draw(self):
        # background
        self.screen.fill((255, 255, 255))
        background = pygame.image.load('images/sudoku_background.png')
        self.screen.blit(background, (0, 0))

        hearts = self.heart_images[self.lives]
        self.screen.blit(hearts, (0, 0))

        for row in range(0, 9):
            for col in range(0, 9):
                self.cells[row][col].draw()

    def decrement_lives(self):
        self.lives -= 1
        if self.lives < 0:
            self.lives = 0

    def set_board(self, new_board):
        self.sudoku = new_board
        for row in range(0, 9):
            for col in range(0, 9):
                self.cells[row][col].set_cell_value(new_board[row][col])

    # method to select a specific cell and draws lines to show selected cell
    def select(self, row, col):
        self.draw()
        pygame.draw.lines(self.screen, (50, 82, 123), True,
                          [(80 * col, 80 * row), (80 * (col + 1), 80 * row), (80 * (col + 1), 80 * (row + 1)),
                           (80 * col, 80 * (row + 1))], 5)
        # pygame.draw.circle(self.screen, (50, 82, 123), ((col * 80) + 40, (row * 80) + 40), 40, 5)
        self.selected_cell = self.cells[col][row]

    # function to calculate the row and col the user clicked on
    def click(self, x, y):
        if x <= self.width and y <= self.height:
            row = y // 80
            col = x // 80
            return row, col
        return None, None

    # sets selected cell's value to 0
    def clear(self):
        # checks if cell is permanent
        if self.selected_cell.original_value == 0:
            self.selected_cell.set_cell_value(0)
            self.selected_cell.set_sketched_value(0)
        self.draw()

    # sets sketch value of cell
    def sketch(self, value):
        self.selected_cell.set_sketched_value(value)
        self.draw()

    # submits the guess value
    def place_number(self, value):
        # checks if cell is permanent
        if self.selected_cell.original_value == 0:
            self.selected_cell.set_cell_value(value)
            self.draw()
            self.update_board()

    # sets all cells back to original value
    def reset_to_original(self):
        for row in range(0, 9):
            for col in range(0, 9):
                self.cells[row][col].set_cell_value(self.cells[row][col].original_value)
                self.cells[row][col].set_sketched_value(0)
        self.draw()
        self.update_board()

    # checks if 2D list is full
    def is_full(self):
        for row in range(0, 9):
            for col in range(0, 9):
                if self.sudoku[row][col] == 0:
                    return False
        return True

    # updates underlying 2D list
    def update_board(self):
        for row in range(0, 9):
            for col in range(0, 9):
                self.sudoku[row][col] = self.cells[row][col].value

    # finds first open cell
    def find_empty(self):
        for row in range(0, 9):
            for col in range(0, 9):
                if self.cells[row][col].value == 0:
                    return row, col

    # clears the red highlights
    def clear_red_highlights(self):
        for row in range(0, 9):
            for col in range(0, 9):
                self.cells[row][col].set_red_highlight(False)

    # checks if board is correct
    def check_board(self, og_board):
        # keeps a copy of original generated board
        original_board = copy.deepcopy(og_board)
        # solves the generated board
        solved_sudoku = sudoku.solve_sudoku(og_board)

        if solved_sudoku == self.sudoku:
            return True
        else:
            self.decrement_lives()
            # redraw the entire board to clear previous red highlights
            self.draw()
            # creates list (row, col, value) with incorrectly inputted cells
            differences = []
            for row in range(0, 9):
                for col in range(0, 9):
                    if self.sudoku[row][col] != solved_sudoku[row][col]:
                        differences.append((row, col, self.sudoku[row][col]))
            # draws lines around incorrectly inputted cells
            for row, col, num in differences:
                pygame.draw.lines(self.screen, (255, 0, 0), True,
                                  [(80 * row, 80 * col), (80 * (row + 1), 80 * col), (80 * (row + 1), 80 * (col + 1)),
                                   (80 * row, 80 * (col + 1))], 5)
            # updates the display to show the differences
            pygame.display.flip()
            return False



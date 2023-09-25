import sudokuGenerator
import board
import pygame
import math, random
import sys


def draw_game_start(screen):
    # initializes fonts
    font = pygame.font.Font('fonts/light.ttf', 25)

    # background image
    color = (255, 255, 255)
    screen.fill(color)
    background = pygame.image.load('images/background.png')
    screen.blit(background, (0, 0))

    list = ['easy', 'medium', 'hard']
    list_position = 0
    difficulty = 0

    # initializes and draws the text
    difficulty_surface = font.render(list[list_position], 0, (105, 105, 105))
    difficulty_rectangle = difficulty_surface.get_rect(
        center=(720 // 2, 400))
    screen.blit(difficulty_surface, difficulty_rectangle)

    # initializes buttons with text
    left_text = font.render("<", 0, (105, 105, 105))
    newGame_text = font.render("new game", 0, (105, 105, 105))
    right_text = font.render(">", 0, (105, 105, 105))

    # initializes the buttons background color
    left_surface = pygame.Surface((left_text.get_size()[0] + 20, left_text.get_size()[1] + 20))
    left_surface.fill((255, 255, 255))
    left_surface.blit(left_text, (10, 10))
    newGame_surface = pygame.Surface((newGame_text.get_size()[0] + 20, newGame_text.get_size()[1] + 20))
    newGame_surface.fill((255, 255, 255))
    newGame_surface.blit(newGame_text, (10, 10))
    right_surface = pygame.Surface((right_text.get_size()[0] + 20, right_text.get_size()[1] + 20))
    right_surface.fill((255, 255, 255))
    right_surface.blit(right_text, (10, 10))

    # initializes buttons rectangles
    left_rectangle = left_surface.get_rect(
        center=(720 // 2 - 150, 400))
    newGame_rectangle = newGame_surface.get_rect(
        center=(720 // 2, 475))
    right_rectangle = right_surface.get_rect(
        center=(720 // 2 + 150, 400))

    # draws the buttons rectangles
    screen.blit(left_surface, left_rectangle)
    screen.blit(newGame_surface, newGame_rectangle)
    screen.blit(right_surface, right_rectangle)

    selectedDifficulty = None
    # loop to determine game mode selected
    while selectedDifficulty is None or False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # loop for left arrow button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if left_rectangle.collidepoint(event.pos):
                    if list_position == -3:
                        list_position = 0
                        difficulty = 0
                    else:
                        list_position -= 1
                        difficulty -= 1
                    # updates background after every click
                    screen.fill(color)
                    background = pygame.image.load('images/background.png')
                    screen.blit(background, (0, 0))

                    # redraws the buttons on screen after every click
                    difficulty_surface = font.render(list[list_position], 0, (105, 105, 105))
                    difficulty_rectangle = difficulty_surface.get_rect(
                        center=(720 // 2, 400))
                    screen.blit(difficulty_surface, difficulty_rectangle)
                    screen.blit(left_surface, left_rectangle)
                    screen.blit(newGame_surface, newGame_rectangle)
                    screen.blit(right_surface, right_rectangle)
                # loop for right arrow button
                elif right_rectangle.collidepoint(event.pos):
                    if list_position == 2:
                        list_position = 0
                        difficulty = 0
                    else:
                        list_position += 1
                        difficulty += 1
                    # updates background after every click
                    screen.fill(color)
                    background = pygame.image.load('images/background.png')
                    screen.blit(background, (0, 0))

                    # redraws the buttons on screen after every click
                    difficulty_surface = font.render(list[list_position], 0, (105, 105, 105))
                    difficulty_rectangle = difficulty_surface.get_rect(
                        center=(720 // 2, 400))
                    screen.blit(difficulty_surface, difficulty_rectangle)
                    screen.blit(left_surface, left_rectangle)
                    screen.blit(newGame_surface, newGame_rectangle)
                    screen.blit(right_surface, right_rectangle)
                # if user clicks new game it returns the difficulty selected
                elif newGame_rectangle.collidepoint(event.pos):
                    selectedDifficulty = difficulty
        pygame.display.update()
    return selectedDifficulty


def win_screen(screen):
    # loads background image
    background = pygame.image.load('images/background.png')
    screen.blit(background, (0, 0))

    # creates font size
    game_font = pygame.font.Font('fonts/regular.ttf', 95)
    # creates text
    win_text = game_font.render('Game Won!', 0, (0, 0, 0))
    win_rectangle = win_text.get_rect(
        center=(720 // 2, 800 // 2 - 150))
    screen.blit(win_text, win_rectangle)
    # creates exit button
    exit_font = pygame.font.Font('fonts/thin.ttf', 45)
    exit_text = exit_font.render('exit', 0, (255, 255, 255))
    exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    exit_surface.fill((255, 165, 0))
    exit_surface.blit(exit_text, (10, 10))
    exit_rectangle = exit_surface.get_rect(
        center=(720 // 2, 1000 // 2))
    screen.blit(exit_surface, exit_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_rectangle.collidepoint(event.pos):
                    return False
        pygame.display.update()


def lose_screen(screen):
    # generates Game Over text
    font = pygame.font.Font('fonts/regular.ttf', 90)
    lose_text = font.render('Game Over :(', 0, (0, 68, 5))
    lose_rectangle = lose_text.get_rect(
        center=(360, 360))
    screen.blit(lose_text, lose_rectangle)

    # generates restart button
    font = pygame.font.Font('fonts/light.ttf', 45)
    newGame_text = font.render("new game", 0, (0, 68, 5))
    newGame_surface = pygame.Surface((newGame_text.get_size()[0] + 50, newGame_text.get_size()[1] + 4))
    newGame_surface.fill((255, 255, 255))
    newGame_surface.blit(newGame_text, (25, 2))
    newGame_rectangle = newGame_surface.get_rect(
        center=(360, 755))
    screen.blit(newGame_surface, newGame_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if newGame_rectangle.collidepoint(event.pos):
                    return True
        pygame.display.update()
    return False


def try_again_screen(screen, difficulty):
    heartPics = ['images/2.png', 'images/1.png', 'images/0.png']
    x = 0
    # generates try again text
    font = pygame.font.Font('fonts/light.ttf', 45)
    tryAgain_text = font.render('Try Again?', 0, "red")
    tryAgain_surface = pygame.Surface((tryAgain_text.get_size()[0] + 25, tryAgain_text.get_size()[1] + 10))
    tryAgain_surface.fill((255, 255, 255))
    tryAgain_surface.blit(tryAgain_text, (10, 5))
    tryAgain_rectangle = tryAgain_surface.get_rect(center=(360, 1525 // 2))
    screen.blit(tryAgain_surface, tryAgain_rectangle)

    hearts = pygame.image.load(heartPics[x])
    screen.blit(hearts, (0, 0))
    x += 1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if tryAgain_rectangle.collidepoint(event.pos):
                    return difficulty
        pygame.display.update()



def solve_sudoku(board):
    def is_valid(num, row, col):
        # checks row and column
        for i in range (9):
            if board[row][i] == num or board[i][col] == num:
                return False
        # checks 3x3 box
        start_row, start_col =  3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == num:
                    return False
        return True

    def solve():
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    for num in range(1, 10):
                        if is_valid(num, row, col):
                            board[row][col] = num
                            if solve():
                                return True
                            # backtrack
                            board[row][col] = 0
                    return False
        return True

    if solve():
        return board
    else:
        return None


def main():
    # initializes board
    pygame.init()
    pygame.display.set_caption('Sudoku')
    width = 720
    height = 800
    screen = pygame.display.set_mode((width, height))
    count = 0
    max_attempts = 3
    # gets difficulty of game
    difficulty = draw_game_start(screen)
    if difficulty is not None and 0 <= difficulty <= 2:
        sudoku_board = board.Board(width, height-80, screen, difficulty)
    else:
        print(difficulty)
        sys.exit()

    clock = pygame.time.Clock()
    running = True
    sudoku_board.draw()

    hearts = pygame.image.load('images/3.png')

    while running is True:
        og_board = sudoku_board.original_board
        # initializes button fonts and size
        font = pygame.font.Font('fonts/thin.ttf', 45)
        # initializes button text
        back_text = font.render(" ", 0, (255, 255, 255))
        restart_text = font.render(" ", 0, (255, 255, 255))
        exit_text = font.render(" ", 0, (255, 255, 255))
        # initializes the buttons background color
        back_surface = pygame.Surface((back_text.get_size()[0] + 20, back_text.get_size()[1] + 20), pygame.SRCALPHA)
        back_surface.blit(back_text, (10, 10))
        restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20),
                                         pygame.SRCALPHA)
        restart_surface.blit(restart_text, (10, 10))
        exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20), pygame.SRCALPHA)
        exit_surface.blit(exit_text, (10, 10))
        # initializes buttons rectangles
        back_rectangle = back_surface.get_rect(
            center=(240, 1525 // 2))
        restart_rectangle = restart_surface.get_rect(
            center=(360, 1525 // 2))
        exit_rectangle = exit_surface.get_rect(
            center=(480, 1525 // 2))
        # draws the buttons rectangles
        screen.blit(back_surface, back_rectangle)
        screen.blit(restart_surface, restart_rectangle)
        screen.blit(exit_surface, exit_rectangle)


        screen.blit(hearts, (0, 0))

        # loop for events
        # pygame.QUIT event means the user clicked X to close window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # statements to determine if buttons where clicked on
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # goes back to main menu
                if back_rectangle.collidepoint(event.pos):
                    difficulty = draw_game_start(screen)
                    sudoku_board = board.Board(width, height - 80, screen, difficulty)
                    sudoku_board.draw()
                # resets board
                elif restart_rectangle.collidepoint(event.pos):
                    sudoku_board.reset_to_original()
                # exits out of program
                elif exit_rectangle.collidepoint(event.pos):
                    running = False

                x, y = pygame.mouse.get_pos()
                row, col = sudoku_board.click(x, y)
                if row is not None:
                    sudoku_board.select(row, col)
                else:
                    sudoku_board.draw()
            # statements to determine keys pressed
            elif event.type == pygame.KEYDOWN:
                try:
                    if event.key == pygame.K_LEFT:
                        col = col - 1
                        sudoku_board.select(row, col)
                    elif event.key == pygame.K_RIGHT:
                        col = col + 1
                        sudoku_board.select(row, col)
                    elif event.key == pygame.K_UP:
                        row = row - 1
                        sudoku_board.select(row, col)
                    elif event.key == pygame.K_DOWN:
                        row = row + 1
                        sudoku_board.select(row, col)
                    elif event.key == pygame.K_RETURN:
                        sudoku_board.place_number(sudoku_board.selected_cell.sketch_value)
                    elif event.key == pygame.K_BACKSPACE:
                        sudoku_board.clear()
                        sudoku_board.select(row, col)
                    else:
                        number = int(chr(event.key))
                        if 9 >= number >= 1:
                            sudoku_board.sketch(number)
                            sudoku_board.select(row, col)
                except ValueError:
                    pass
                except TypeError:
                    pass
                # checks if board is full
                if sudoku_board.is_full() is True:
                    # checks if solved board matches users board
                    og_board = sudoku_board.original_board
                    win = sudoku_board.check_board(og_board)
                    # win function
                    if win is True:
                        running = win_screen(screen)
                    # try again function
                    else:
                        # add 1 to count
                        count += 1
                        # if count >= 3 then lose screen
                        if count >= max_attempts:
                            running = lose_screen(screen)
                            # redraws new board
                            if running:
                                difficulty = draw_game_start(screen)
                                sudoku_board = board.Board(width, height - 80, screen, difficulty)
                                sudoku_board.draw()
                            # resets count back to 0
                            count = 0
                        # if count is not 3 then try again screen
                        else:
                            try_again_screen(screen, difficulty)
                            # resets board
                            if running:
                                sudoku_board.reset_to_original()
                                sudoku_board.draw()

        # flip() the display to put your work on screen
        pygame.display.update()
        pygame.display.flip()
        clock.tick(60)  # limits FPS to 60

    pygame.quit()


if __name__ == '__main__':
    main()
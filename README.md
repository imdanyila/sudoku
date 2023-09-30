# sudoku

This is a Python program that allows you to play Sudoku and includes a solver to automatically complete the generated Sudoku puzzle. You can also restart the game, access a win screen if you solve the puzzle, and try again if you lose, but if you fail three times then a lose screen is presented.

## How to Play

1. Run the program using Python.
2. The game will start, and you'll see a menu to select the difficulty level (easy, medium, or hard).
3. Once you select the difficulty, the Sudoku puzzle will be displayed on the screen.
4. You can navigate through the puzzle using the arrow keys or the mouse.
5. To input a number, select the cell and type the number on your keyboard.
6. To delete a number, select the cell and press the backspace key.
7. The board will automatically check if it was correctly solved once board is full.
8. If you complete the puzzle correctly, you'll see a win screen. You can start a new game from there.
9. If you can't solve the puzzle, you'll see a lose screen with the option to try again (You have three tries).
10. To return to the main menu, you can click the back button.
11. To completely reset the board, you can click the restart button.
12. To exit the program entirely, you can click the 'X'.

## Code Structure

- `sudoku.py`: The main program that integrates the puzzle generator, the board, and the game loop using the Pygame library.
- `sudokuGenerator.py`: This module generates valid Sudoku puzzles of varying difficulty levels.
- `board.py`: Contains the `Board` class responsible for managing the Sudoku board during gameplay.

## Dependencies

- Python 3.x
- Pygame (make sure it's installed)

## How to Run

1. Clone this GitHub repository: [https://github.com/imdanyila/sudoku.git]
2. Navigate to the project directory.
3. Run `sudoku.py` using Python.

## Acknowledgments

- This project uses the Pygame library for graphics and user interaction.
- The Sudoku puzzle generator is based on an algorithm for generating valid Sudoku puzzles.

Have fun playing Sudoku and improving your puzzle-solving skills!

# Sudoku

An interactive Python-programmed sudoku puzzle that a user interfaces with on a CLI. Sudoku board is graphically displayed in a CLI, and incrementally filled a user chooses which spaces to fill on the board. 

The program has a verificaton method that checks for correct solutions. Currently, there is one hard-coded valid sudoku puzzle supplied with the program but the program can use virtually any valid sudoku puzzle. There is also a clear board method that clears all spaces filled by the user. 

## Instructions:

Required: Latest version of Python3 installed

The rules of sudoku are as follows: each unique number can only be present once in each row, each unique number can only be present once in each column, and each unique number can only be present once in each 3 x 3 region. For a 9 x 9 puzzle, the unique numbers range from 1 to 9. Hence, in a row, column, or region each of the unique numbers must be present once.

1. Execute ```python sudoku.py``` on a CLI.
2. the user is prompted to choose 1 of 4 options: ```Enter (1) Fill board, (2) verify your solution, (3) clear board, or (4) exit:```
3. On startup and everytime the user fills a space on the board, the current state of the sudoku board is outputted in the CLI:

  _   [ 5 ]   _    |    _     _   [ 9 ]  |  [ 8 ] [ 1 ] [ 3 ] 


[ 9 ] [ 8 ]   _    |  [ 3 ] [ 5 ]   _    |  [ 6 ]   _   [ 7 ] 


[ 6 ]   _     _    |    _   [ 8 ]   _    |  [ 5 ] [ 9 ] [ 4 ] 

____________________________________________________________  
[ 8 ] [ 3 ] [ 2 ]  |    _     _   [ 6 ]  |    _     _     _   


[ 7 ]   _     _    |  [ 1 ] [ 2 ] [ 8 ]  |    _     _   [ 9 ]


[ 1 ] [ 9 ]   _    |    _   [ 7 ] [ 3 ]  |  [ 2 ]   _     _

____________________________________________________________
[ 3 ] [ 7 ]   _    |  [ 6 ] [ 9 ]   _    |    _   [ 5 ]   _


  _   [ 2 ]   _    |    _     _     _    |  [ 7 ]   _     _


  _     _     _    |    _     _   [ 4 ]  |    _     _     _

4. Enter ```1``` to begin filling the board. The program will prompt the user to choose a row, column, and value. 
5. Continue entering in values until the board is filled with your solution.
6. Enter ```x``` to return to the previous 4 option prompt.
7. Enter ```2``` to check if your solution is correct.
8. At any time, the user can return to the 4 option prompt and clear their board by entering ```3```.
9. To exit the program from the 4 option prompt, enter ```4```.


## Notes

Next steps: A feature that allows a user to choose between an assortment of supplied sudoku puzzles on program start up. Undo functionality that allows a user to revert their previous input on the sudoku board.


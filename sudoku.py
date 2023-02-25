import sys


class Sudoku:
    """
    represents a game of sudoku;
    """

    def __init__(self, board, board_template):
        """
        receives list parameters board and board_template;
        initializes Sudoku object with private data members:
            self._board_template;
            self._board;
            self._contents
        self._board is set to board
        self._board_template is set ot board_template
        self._contents is initialized as a list containing all possible unique puzzle numbers;
        """

        self._board_template = board_template

        self._board = board

        self._contents = []
        for i in range(1, len(self._board) + 1):        # creates a list containing all possible unique values
            self._contents.append(str(i))

    def enter_cell(self):
        """
        receives None;
        called in options method;
        enables a user to fill a cell in puzzle grid via input prompts;
        verifies valid user input;
        calls itself until user enters 'x', in which case options is called;
        returns None
        """
        row = input("Enter the row number of your chosen cell, or"
                    " exit back to options by entering 'x': ")
        if row == "x":
            self.options()
        column = input("Enter the column number of your chosen cell, or"
                       " exit back to options by entering 'x': ")
        if column == 'x':
            self.options()
        if " " in row or " " in column:
            print("This is not valid input.")
            self.enter_cell()
        try:
            if 1 > int(row) or int(row) > len(self._board):
                print("That is not a valid cell.")
                self.enter_cell()

            elif 1 > int(column) or int(column) > len(self._board):
                print("That is not a valid cell.")
                self.enter_cell()

        except ValueError:
            print("This is not valid input")
            self.enter_cell()

        if self._board_template[int(row) - 1][int(column) - 1] != " ":      # stops user from changing hard-coded
            print("This cell is an original and cannot be changed.")        # puzzle grid cells
            self.enter_cell()
        else:
            cell_input = input("Enter a value (1 - 9) for that cell: ")
            self._board[int(row) - 1][int(column) - 1] = cell_input
            print("Input entered.")
            self.print_board()
            self.enter_cell()

    def verification(self):
        """
        receives None
        contains three sets of nested loops that check that every row, column, and square region is only filled with
            unique numbers;
        notifies the user whether the puzzle is incomplete, incorrect, or correct;
        calls options after verifying user solution;
        returns None
        """
        for row in self._board:                                
            list_check = []
            for cell in row:                                   
                if cell == " ":
                    print("Incomplete solution.")
                    self.options()
                else:
                    list_check.append(cell)                     
            list_check.sort()                                   
            if list_check != self._contents:                   
                print("Duplicate number found in row. Incorrect solution.")
                self.options()

        length = len(self._board)                       # length of sudoku board
        len_of_region = length ** 0.5                   # length of square region in sudoku board
        len_of_region = int(len_of_region)

        for i in range(length):                                 
            list_check = []
            for j in range(length):                             
                if self._board[j][i] == " ":
                    print("Incomplete solution.")
                    self.options()
                else:
                    list_check.append(self._board[j][i])        
            list_check.sort()                                   
            if list_check != self._contents:                    
                print("Duplicate number found in column. Incorrect solution.")
                self.options()

        for i in range(0, length, len_of_region):               
            for j in range(0, length, len_of_region):           
                list_check = []
                for z in range(len_of_region):                  
                    list_check = list_check + self._board[i + z][j:j + len_of_region]  
                list_check.sort()                               
                if list_check != self._contents:                
                    print("Duplicate number or empty cell found in region. Incorrect solution.")
                    self.options()

        print("Your solution is correct!")
        self.options()

    def restart(self):
        """
        receives None;
        resets sudoku board;
        calls options;
        returns None;
        """
        for i in range(len(self._board)):
            for j in range(len(self._board)):
                self._board[i][j] = self._board_template[i][j]
        print("Sudoku board cleared.")
        self.options()

    def print_board(self):
        """
        receives None;
        outputs current sudoku board to terminal;
        returns None;
        """
        length = len(self._board)
        len_of_region = length ** 0.5
        len_of_region = int(len_of_region)

        curr_row = 1
        curr_column = 1
        for row in self._board:
            for element in row:
                if self._board_template[curr_row - 1][curr_column - 1] != " ":
                    print("[", element, "]", end=" ")
                elif element == " ":
                    print("  _   ", end="")
                else:
                    print(" ", element, end="   ")
                if curr_column == length:
                    print("")
                elif curr_column % len_of_region == 0:
                    print(end=" |  ")
                if curr_column == length:
                    curr_column = 0
                curr_column += 1
            if curr_row == length:
                print("\n")
            elif curr_row % len_of_region == 0:
                print("\n____________________________________________________________")
            else:
                print("\n")
            curr_row += 1

    def options(self):
        """
        receives None
        input prompts a user to pick one of four options and calls method associated to chosen option;
            fill a cell on the board;
            verify user's solution;
            reset the board;
            end game;
        returns None
        """
        option = input(" Enter (1) Fill board, (2) verify your solution, (3) clear board, or (4) exit: ")
        if option == "1":
            print("Here is the board so far.")
            self.print_board()
            self.enter_cell()
        elif option == "2":
            self.verification()
        elif option == "3":
            self.restart()
        elif option != "4":
            self.options()
        else:
            sys.exit()


def main():
    # board_solution = [["2", "5", "7", "4", "6", "9", "8", "1", "3"],
    #          ["9", "8", "4", "3", "5", "1", "6", "2", "7"],
    #          ["6", "1", "3", "2", "8", "7", "5", "9", "4"],
    #          ["8", "3", "2", "9", "4", "6", "1", "7", "5"],
    #          ["7", "4", "5", "1", "2", "8", "3", "6", "9"],
    #          ["1", "9", "6", "5", "7", "3", "2", "4", "8"],
    #          ["3", "7", "8", "6", "9", "2", "4", "5", "1"],
    #          ["4", "2", "9", "8", "1", "5", "7", "3", "6"],
    #          ["5", "6", "1", "7", "3", "4", "9", "8", "2"]]

    board_template = [[" ", "5", " ", " ", " ", "9", "8", "1", "3"],
            ["9", "8", " ", "3", "5", " ", "6", " ", "7"],
            ["6", " ", " ", " ", "8", " ", "5", "9", "4"],
            ["8", "3", "2", " ", " ", "6", " ", " ", " "],
            ["7", " ", " ", "1", "2", "8", " ", " ", "9"],
            ["1", "9", " ", " ", "7", "3", "2", " ", " "],
            ["3", "7", " ", "6", "9", " ", " ", "5", " "],
            [" ", "2", " ", " ", " ", " ", "7", " ", " "],
            [" ", " ", " ", " ", " ", "4", " ", " ", " "]]

    board = board_template.copy()

    game = Sudoku(board, board_template)
    game.options()


if __name__ == "__main__":
    main()

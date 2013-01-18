class Board:
    board = []
    
    def __init__(self, rows, cols):
        for row in range(rows):
            self.board += [["# "] *cols]

    def setTile(self, row, col, char):
        print("dummy code")
        self.board[row][col] = char

    def getTile(self, row, col):
        return self.board[row][col]

    #NOTE THAT CURSES MODE MUST BE SET UP BEFORE PRINTING
    #TO THE SCEEN, ELSE YOU WILL GET ERRORS.
    def printBoard(self, screen):
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                screen.addstr(self.board[row][col])

            screen.addstr("\n")

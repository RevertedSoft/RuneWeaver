#Rune Weaver 2 v. 0.01
#Copyright (c) 2013 RevertedSoft <revertedsoft.com>
#
#Permission is hereby granted, free of charge, to any person obtaining a copy 
#of this software and associated documentation file (the "Software"), to deal 
#with the Software without limitation in the rights to use, copy, modify, merge 
#publish, distribute, but NOT to sell copies of the Software, subject to the 
#following condition:
#
#The above copyright notice and this permission notice shall be included in all 
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
#SOFTWARE.

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

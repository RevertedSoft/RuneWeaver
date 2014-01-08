#Rune Weaver v. 0.01
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

import random
from .board import Board


class World(Board):
    def __init__(self, rows, cols):
        Board.__init__(self, rows, cols)
        self.generateWorld()

    def generateWorld(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                self.board[row][col] = ' '
                
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if row == 0 or row == len(self.board) -1 or col == 0 or col == len(self.board[0]) -1:
                    self.board[row][col] = '#'

##                elif random.random() < 0.35:
##                    self.board[row][col] = '#'

    def printWorld(self, screen, creatureList, background):
        
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                screen.putchar(self.board[row][col], row, col)

        for creatures in creatureList[:]:
            screen.putchar(creatures.symbol, creatures.positionX, creatures.positionY, creatures.color, background)

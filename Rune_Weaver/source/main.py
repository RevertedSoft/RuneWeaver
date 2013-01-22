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

''' This module holds the main method.'''

import curses

from . import creature, equipment, player
from .globs import *
from .world import *

def main():
    #setup curses mode
    display = curses.initscr()
    curses.noecho()
    curses.cbreak()

    playerOne = player.Player('some name', 5, 5);
    mainWorld = World(20, 20)
    mainWorld.printBoard(display)

    display.refresh()
    display.getch()

    #end curses mode
    curses.nocbreak(); curses.echo()
    curses.endwin()
    pass

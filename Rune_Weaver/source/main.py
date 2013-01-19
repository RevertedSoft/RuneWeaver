''' This module holds the main method.'''
import curses

from . import creature, equipment, player
from .globs import *
from .world import World

def main():
	#setup curses mode
	display = curses.initscr()
	curses.noecho()
	curses.cbreak()
	
	mainWorld = World(20, 20)
	mainWorld.printBoard(display)
	
	display.refresh()
	display.getch()
	
	#end curses mode
	curses.nocbreak(); curses.echo()
	curses.endwin()
	pass

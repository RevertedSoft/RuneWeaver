from .board import Board

class World(Board):
	def __init__(self, rows, cols):
		Board.__init__(Board, rows, cols)
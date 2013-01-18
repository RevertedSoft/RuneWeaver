''' This module contains everything related to the player.'''
from . import creature

class Player(creature.Humanoid):

    def __init__(self):

        creature.Humanoid.__init__(self)

        self.level = 1

    def gainExperience(self, experience):
        self.experience += experience

    def checkLevelUp(self):
        if self.experience == self.level * self.level * 100:
            return True
        else:
            return False

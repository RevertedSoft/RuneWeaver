''' This module contains everything related to the player.'''
from . creature import Humanoid

class Player(Humanoid):

    def __init__(self):

        Humanoid.__init__(self)

        self.level = 1

    def gainExperience(self, experience):
        self.experience += experience

    def checkLevelUp(self):
        if self.experience == self.level * self.level * 100:
            return True
        else:
            return False

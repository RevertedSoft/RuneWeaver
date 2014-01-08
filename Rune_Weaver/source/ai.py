#this module contains ai methods, generic ai methods will be used by the rest of the advanced ai
from .globs import *


class AI():

    def __init__(self, creature, creatureList, world):
        pass
        self.creature = creature
        self.creatureList = creatureList
        self.world = world
        
    def wander(self):
        #this method will occasionally move the self.creature around
        doIWander = random.randint(0,20)
        if doIWander > 18:
            wanderDirection = random.randint(0,3)
            if wanderDirection == 0:
                if self.world.getTile(self.creature.positionX -1, self.creature.positionY) != '#':
                    self.creature.positionX -= 1
            elif wanderDirection == 1:
                if self.world.getTile(self.creature.positionX +1, self.creature.positionY) != '#':
                    self.creature.positionX += 1
            elif wanderDirection == 2:
                if self.world.getTile(self.creature.positionX, self.creature.positionY -1) != '#':
                    self.creature.positionY -= 1
            elif wanderDirection == 3:
                if self.world.getTile(self.creature.positionX, self.creature.positionY +1) != '#':
                    self.creature.positionY += 1


class Passive(AI):

    def __init__(self, creature, creatureList, world):
        AI.__init__(self, creature, creatureList, world)

    def behavior(self):
        self.creature.checkDeath()
        self.wander()
    


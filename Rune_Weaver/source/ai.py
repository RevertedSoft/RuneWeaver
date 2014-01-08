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

    def getTarget(self):
        #this method randomly chooses a target from the creatures proximityList
        potentialTargets = []
        self.creature.checkProximity(self.creatureList)
        #determine what creatures the current ai wants to attack
        for creatures in self.creature.proximityList:
            if creatures != None:
                if creatures.faction != self.creature.faction:
                    potentialTargets.append(creatures)

        #now choose a random target
        if len(potentialTargets) > 1:
            targetCreature = random.randint(0, len(potentialTargets) - 1)
            self.creature.target = potentialTargets[targetCreature]
        elif len(potentialTargets) == 1:
            self.creature.target = potentialTargets[0]
        else:
            self.creature.target = None

    def attackTarget(self):
        if self.creature.target != None:
            self.creature.dealDamage(self.creature.target)

    def flee(self):
        if self.creature.currentHealth < self.creature.maxHealth/2:
            doIFlee = random.randint(0,20)
            if doIFlee > 7:
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

                print(self.creature.name + " is fleeing!")
            
                


class Passive(AI):

    def __init__(self, creature, creatureList, world):
        AI.__init__(self, creature, creatureList, world)

    def behavior(self):
        self.creature.checkDeath()
        self.wander()
        self.flee()

class Defensive(AI):

    def __init__(self, creature, creatureList, world):
        AI.__init__(self, creature, creatureList, world)

    def behavior(self):
        self.creature.checkDeath()
        self.getTarget()
        self.attackTarget()
        self.flee()

class Wanderer(AI):

    def __init__(self, creature, creatureList, world):
        AI.__init__(self, creature, creatureList, world)

    def behavior(self):
        self.creature.checkDeath()
        self.wander()
        self.getTarget()
        self.attackTarget()
        self.flee()
    


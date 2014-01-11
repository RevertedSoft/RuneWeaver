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

from .globs import *

class AI():
    """The AI class represents the basic ai functions that will be used by other AI subclasses.
       attributes:
           creature --- the creature that is inheriting the ai
           creatureList --- a list of the creatures currently in the game (later a list of the creatures the creature is aware of)
           world --- an object representing the world(later the map the creature is currently aware of)

        methods:
            wander(self, chance): --- the creature will randomly decide whether it needs to wander every turn depending on the chance argument it is passed
            getTarget(self): --- the creature will randomly select a target from its proximityList
            attackTarget(self): --- the creature will attack the target it selected
            flee(self, chance): --- the creature will have a chance to flee in a random direction once it falls under half health"""

    def __init__(self, creature, creatureList, world):
        
        self.creature = creature
        self.creatureList = creatureList
        self.world = world
        
    def wander(self, chance=2):
        if not self.creature.dead:
        #this method will occasionally move the self.creature around
            doIWander = random.randint(0,20)
            if doIWander > (20 - chance):
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
        if not self.creature.dead:
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
        if not self.creature.dead:
            if self.creature.target != None:
                self.creature.dealDamage(self.creature.target)

    def flee(self, chance=7):
        if not self.creature.dead:
            if self.creature.currentHealth < self.creature.maxHealth/2:
                doIFlee = random.randint(0,20)
                if doIFlee > (20-chance):
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
                    eventLog.printToDisplay(self.creature.name + " is fleeing!")
            
                
class Passive(AI):

    def __init__(self, creature, creatureList, world):
        AI.__init__(self, creature, creatureList, world)

    def behavior(self):
        self.creature.checkDeath()
        self.wander(3)
        self.flee(18)

class Defensive(AI):

    def __init__(self, creature, creatureList, world):
        AI.__init__(self, creature, creatureList, world)

    def behavior(self):
        self.creature.checkDeath()
        self.getTarget()
        self.attackTarget()
        self.flee(5)

class Wanderer(AI):

    def __init__(self, creature, creatureList, world):
        AI.__init__(self, creature, creatureList, world)

    def behavior(self):
        self.creature.checkDeath()
        self.wander(8)
        self.getTarget()
        self.attackTarget()
        self.flee(6)
    


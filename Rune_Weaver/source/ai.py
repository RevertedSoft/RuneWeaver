#Rune Weaver v. 0.01
#Copyright (c) 2013 - 2014 RevertedSoft <revertedsoft.com>
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
        #self.pursueTarget = None
        
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
                self.creature.pursueTarget = None
                self.creature.pursueTargetList == []
            elif len(potentialTargets) == 1:
                self.creature.target = potentialTargets[0]
                self.creature.pursueTarget = None
                self.creature.pursueTargetList == []
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

    def pursue(self, distance=3):
        ### TODO NEEDS LOTS OF WORK

        if not self.creature.dead:
            if self.creature.target != None:
                if self.creature.target.dead:
                    self.creature.target == None
            if self.creature.target == None:
                if self.creature.pursueTarget == None:
                    for creatures in self.creatureList[:]:
                        #decide if there is a creature in range for the current creature to pursue
                        if creatures.positionX >= (self.creature.positionX - distance) and creatures.positionX <= (self.creature.positionX + distance) and creatures.positionY >= (self.creature.positionY - distance) and creatures.positionY <= (self.creature.positionY + distance):
                            if creatures.faction != self.creature.faction:
                                self.creature.pursueTargetList.append(creatures)

                                #now choose a random target
                                if len(self.creature.pursueTargetList) > 1:
                                    targetSelect = random.randint(0, len(self.creature.pursueTargetList) - 1)
                                    self.creature.pursueTarget = self.creature.pursueTargetList[targetSelect]
                                    
                                    print(self.creature.name + " is pursuing " + self.creature.pursueTarget.name)
                                elif len(self.creature.pursueTargetList) == 1:
                                    self.creature.pursueTarget = self.creature.pursueTargetList[0]
                                    
                                    print(self.creature.name + " is pursuing " + self.creature.pursueTarget.name)


                #determine which direction the selected target is facing and move toward it
                if self.creature.pursueTarget != None:
                    if self.creature.pursueTarget.positionX < self.creature.positionX:
                        if self.world.getTile(self.creature.positionX -1, self.creature.positionY) != '#':
                            self.creature.positionX -= 1
                    elif self.creature.pursueTarget.positionX > self.creature.positionX:
                        if self.world.getTile(self.creature.positionX +1, self.creature.positionY) != '#':
                            self.creature.positionX += 1
                    elif self.creature.pursueTarget.positionY < self.creature.positionY:
                        if self.world.getTile(self.creature.positionX, self.creature.positionY -1) != '#':
                            self.creature.positionY -= 1
                    elif self.creature.pursueTarget.positionY > self.creature.positionY:
                        if self.world.getTile(self.creature.positionX, self.creature.positionY +1) != '#':
                            self.creature.positionY += 1


    def finish(self):
        del self

                                
                    
            
                
class Passive(AI):

    def __init__(self, creature, creatureList, world):
        AI.__init__(self, creature, creatureList, world)

    def behavior(self):
        self.creature.checkDeath()
        if self.creature.dead:
            self.finish()
        self.wander(3)
        self.flee(18)

class Defensive(AI):

    def __init__(self, creature, creatureList, world):
        AI.__init__(self, creature, creatureList, world)

    def behavior(self):
        self.creature.checkDeath()
        if self.creature.dead:
            self.finish()
        self.getTarget()
        self.attackTarget()
        self.flee(5)

class Wanderer(AI):

    def __init__(self, creature, creatureList, world):
        AI.__init__(self, creature, creatureList, world)

    def behavior(self):
        self.creature.checkDeath()
        if self.creature.dead:
            self.finish()
        self.wander(8)
        self.getTarget()
        self.attackTarget()
        self.flee(6)
        self.pursue()

    


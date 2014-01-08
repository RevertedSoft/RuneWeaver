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

""" This module contains everything related to the player."""
from . creature import *
import pygame
from pygame.locals import *
from .globs import *


class Player(Humanoid):

    def __init__(self, name, positionX, positionY, symbol, color):

        Humanoid.__init__(self, name, positionX, positionY, symbol, color)

        self.level = 1

    def gainExperience(self, experience):
        self.experience += experience

    def checkLevelUp(self):
        if self.experience == (self.level * self.level) * 100:
            return True
        else:
            return False
            

    def turn(self, creatureList):

        #set the noAction flag for continuing the event loop
        noAction = True

        while noAction:

            #check if the player is dead
            self.checkDeath()
            if self.dead:
                return False
            #check for any creatures within proximity of the player
            self.checkProximity(creatureList)
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    return False

                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        exitGame()

                    elif event.key == K_UP:
                        
                        if dungeon[floor].getTile(self.positionX, self.positionY -1) != '#':
                            
                            if self.proximityList[0] != None:
                                
                                print('There is a ' + self.proximityList[0].name + ' there.')
                            else:
                                self.positionY -= 1
                                print('UP')
                                noAction = False

                    elif event.key == K_DOWN:
                        if dungeon[floor].getTile(self.positionX, self.positionY +1) != '#':
                            
                            if self.proximityList[1] != None:
                                print('There is a ' + self.proximityList[1].name + ' there.')
                            else:
                                self.positionY += 1
                                print('DOWN')
                                noAction = False

                    elif event.key == K_LEFT:
                        if dungeon[floor].getTile(self.positionX -1, self.positionY) != '#':
                            if self.proximityList[2] != None:
                                print('There is a ' + self.proximityList[2].name + ' there.')
                            else:
                                self.positionX -= 1
                                print('LEFT')
                                noAction = False

                    elif event.key == K_RIGHT:
                        if dungeon[floor].getTile(self.positionX +1, self.positionY) != '#':
                            if self.proximityList[3] != None:
                                print('There is a ' + self.proximityList[3].name + ' there.')
                            else:
                                self.positionX += 1
                                print('RIGHT')
                                noAction = False

        return True
        

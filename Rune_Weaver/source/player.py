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

""" This module contains everything related to the player."""
from . creature import *
import pygame
from pygame.locals import *
from .globs import *


class Player(Humanoid):

    def __init__(self, name, positionX, positionY, symbol, color, faction, strength, constitution, dexterity, agility, intelligence, wisdom, experience, gold, headArmor=None, shoulderArmor=None, torsoArmor=None, legArmor=None, footArmor=None,weapon=None, shield=None):

        Humanoid.__init__(self, name, positionX, positionY, symbol, color, faction, strength,constitution, dexterity, agility, intelligence, wisdom, experience, gold, None, headArmor, shoulderArmor, torsoArmor, legArmor, footArmor, weapon, shield)
        #equip some armor, only temprorary
        self.headArmor = ARMORLIST[2]
        self.torsoArmor = ARMORLIST[1]
        self.legArmor = ARMORLIST[3]
        self.footArmor = ARMORLIST[4]
        self.shoulderArmor = ARMORLIST[5]
        self.shield = SHIELDLIST[1]
        self.weapon = WEAPONLIST[1]

        self.level = 1

        self.calculateArmor()
        

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
                print("You have died...")
                eventLog.printToDisplay("You have died...")
                return False

            #check for any creatures within proximity of the player
            self.checkProximity(creatureList)
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    return False

                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        exitGame()

                    elif event.key == K_w or event.key == K_UP:
                        if not inputBox.isActive:
                        
                            if dungeon.getTile(self.positionX, self.positionY -1) != '#':
                                
                                if self.proximityList[0] != None:
                                    
                                    print('There is a ' + self.proximityList[0].name + ' there.')
                                    eventLog.printToDisplay('There is a ' + self.proximityList[0].name + ' there.')
                                    self.target = self.proximityList[0]
                                    self.dealDamage(self.target)
                                    noAction = False
                                else:
                                    self.positionY -= 1
                                    print('UP')
                                    eventLog.printToDisplay('UP')
                                    noAction = False

                    elif event.key == K_s or event.key == K_DOWN:
                        if not inputBox.isActive:
                            if dungeon.getTile(self.positionX, self.positionY +1) != '#':
                                
                                if self.proximityList[1] != None:
                                    print('There is a ' + self.proximityList[1].name + ' there.')
                                    eventLog.printToDisplay('There is a ' + self.proximityList[1].name + ' there.')
                                    self.target = self.proximityList[1]
                                    self.dealDamage(self.target)
                                    noAction = False
                                else:
                                    self.positionY += 1
                                    print('DOWN')
                                    eventLog.printToDisplay('DOWN')
                                    noAction = False

                    elif event.key == K_a or event.key == K_LEFT:
                        if not inputBox.isActive:
                            if dungeon.getTile(self.positionX -1, self.positionY) != '#':
                                if self.proximityList[2] != None:
                                    print('There is a ' + self.proximityList[2].name + ' there.')
                                    eventLog.printToDisplay('There is a ' + self.proximityList[2].name + ' there.')
                                    self.target = self.proximityList[2]
                                    self.dealDamage(self.target)
                                    noAction = False
                                else:
                                    self.positionX -= 1
                                    print('LEFT')
                                    eventLog.printToDisplay('LEFT')
                                    noAction = False

                    elif event.key == K_d or event.key == K_RIGHT:
                        if not inputBox.isActive:
                            if dungeon.getTile(self.positionX +1, self.positionY) != '#':
                                if self.proximityList[3] != None:
                                    print('There is a ' + self.proximityList[3].name + ' there.')
                                    eventLog.printToDisplay('There is a ' + self.proximityList[3].name + ' there.')
                                    self.target = self.proximityList[3]
                                    self.dealDamage(self.target)
                                    noAction = False
                                else:
                                    self.positionX += 1
                                    print('RIGHT')
                                    eventLog.printToDisplay('RIGHT')
                                    noAction = False

                    elif event.key == K_RETURN:
                        if not inputBox.isActive:
                            inputBox.isActive = True
                            return [True, True]
                        else:
                            inputBox.isActive = False
                            #print(inputBox.text)
                            eventLog.printToDisplay(inputBox.text[0].text_)#inputBox.text[0])
                            inputBox.alterText([ui.Text("", (0,0))])
                            #print(inputBox.text)
                            return [True, True]

                    if inputBox.isActive:
                        if event.key != K_RETURN:
                            inputBox.typing(event.unicode)
                        return [True, True]

        return [True, False]
        

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

""" This module holds the main method."""

import pygame, sys
from pygame.locals import *
from . import pygcurse, equipment, player, creature
from .globs import *

#create the player variable ###PLACEHOLDER###
playerChar = player.Player("player",20,5,'@','red',factionDict['player'],10,10,10,10,10,10,0,50)

#create new creatures ###TODO### TEMPORARY

newCreature1 = creature.Humanoid("goblin", 15,5,'G', "green", experience=10, ai="passive", faction=factionDict["goblins"])
newCreature2 = creature.Humanoid("goblin", 25,5,'G', "green", experience=10, ai="defensive", faction=factionDict["goblins"])
newCreature3 = creature.Humanoid("goblin", 15,10,'G', "green", experience=10, ai="defensive", faction=factionDict["goblins"])
newCreature4 = creature.Humanoid("Orc", 15,12,'O', "blue", strength=12, constitution=12, faction=factionDict["monsters"], ai="wanderer", weapon = WEAPONLIST[1])
newCreature5 = creature.Humanoid("Hobgoblin", 16,12,'H', "green", strength=17, constitution=15, faction=factionDict["goblins"], ai="wanderer", weapon = WEAPONLIST[1], torsoArmor=ARMORLIST[1])

creatureList = []
creatureList.append(playerChar)
creatureList.append(newCreature1)
creatureList.append(newCreature2)
creatureList.append(newCreature3)
creatureList.append(newCreature4)
creatureList.append(newCreature5)

def exitGame():
    pygame.quit()
    sys.exit()

def main():
    #make the pygcurse window
    

    testButton = ui.Button((1,2), (10,3), win, [["Test",(1,1)]], True, (255,0,0), (0,0,255), (255,0,0))

    userinterface = ui.Menu((40,0), (20,40), win, [["Player",(1,1)]], True, (0,255,0), [testButton])
    

    play = True

    while play == True:
        
        
        dungeon.printWorld(win, creatureList, BLACK)
        #change the userinterface every iteration
        userinterface.alterText([[playerChar.name + " HP:" + str(playerChar.currentHealth) + "/" + str(playerChar.maxHealth),(1,1)], ["STR: " + str(playerChar.strength), (1,5)], ["CON: " + str(playerChar.constitution), (1,6)]])
        userinterface.printMenu()
        eventLog.printUI()
        win.update()
        win.fill((' '))
        play = playerChar.turn(creatureList)
        for creatures in creatureList[1:]:
            ai = creatures.ai(creatures, creatureList, dungeon)
            ai.behavior()
            if creatures.dead:
                creatureList.remove(creatures)
        

    exitGame()

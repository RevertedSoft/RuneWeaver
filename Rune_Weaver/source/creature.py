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

""" This module contains the superclass creature, all other monsters and the player, will inherit from this class."""
import random
from . import ai
from .globs import *

colorDict = {'red':(255,0,0),
             'blue':(0,0,255),
             'white':(255,255,255),
             'green':(0,255,0)}

aiDict = {'passive':ai.Passive,
          'defensive':ai.Defensive}


class Creature():
    """This class is the base class for all creatures in the game.

    attributes:
        strength -- determine the creatures max health, also applies bonuses to the creatures physical damage
        constitution -- determine the creatures max health, also applies small bonuses to physical damage resistance
        dexterity -- applies bonuses to the creatures evasion
        agility -- applies bonuses to the creatures speed
        intelligence -- applies bonuses to magic damage, determines the size of the rune pallete
        wisdom -- applies bonuses to armor and magic resistance, also helps determine the creatures speed with magic
        experience -- this attribute works 2 ways, it represents the players current experience, and it represents how much experience a player will gain from killing a monster
        gold -- # how much gold the creature is worth when killed, also used to represent how much gold the player has

        maxHealth -- maximum health of the creature
        currentHealth -- current health of the creature
        palleteSize -- the maximum number of runes a creature can hold in a spell at any time
        runePallate -- the empty list of runes the creature has summoned
        armor --
        magicRes --
        evasion --
        speed -- is used to determine how often the creature can do physical actions
        magicSpeed -- speed is used to determine how often the creature can do magical actions
        crushRes -- is the crush resistance for the damage type crushing
        piercRes -- is the pierce resistance for the damage type piercing
        slashRes -- is the slash resistance for the damage type slashing
        damage -- base damage of the creature unarmed
        attRange -- base attack range of the creature

        dead --
        action -- when this value reaches 100 the creature is ready to make a physical action
        magicAction -- when this value reaches 100 the creature is ready to make a magic action
        isTurn -- is it the creatures physical turn?
        isMagicTurn -- is it the creatures magic turn?
        targetList -- this list determines all creatures in range that the creature is able to attack
        target -- this is the target the creature has determined it wants to attack

    methods:
        dealDamage -- deals damage to another creature
        takeDamage -- calculates current health after taking damage
        checkDeath -- checks if the creature is dead
        turn --

    """
    def __init__(self, name, positionX=-1, positionY=-1, symbol = "@", color="red", faction="Neutral", strength=5, constitution=5, dexterity=5, agility=5, intelligence=5, wisdom=5, experience=0, gold=0, ai='passive'):
        """Base constructor method for creatures."""
        self.name = name
        #position of the creature
        self.positionX = positionX
        self.positionY = positionY
        self.symbol = symbol
        self.color = colorDict[color]
        #attributes of the creature
        self.strength = strength
        self.constitution = constitution
        self.dexterity = dexterity
        self.agility = agility
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.experience = experience
        self.gold = gold
        #creatures faction
        self.faction = faction
        #initialize secondary attributes that are determined from the primary attributes
        self.maxHealth = int(10 + (self.constitution + (self.strength / 2)))  # TODO: this is not right
        self.currentHealth = self.maxHealth
        self.palleteSize = (self.intelligence // 3)  # TODO: this is not right
        self.runePallate = []
        #self.calculateArmor()
        self.magicRes = (self.intelligence // 6) + (self.wisdom // 3)
        self.evasion = self.dexterity//2
        self.speed = 10 + (self.agility//2)
        self.magicSpeed = 10 + (self.wisdom//2)
        self.crushRes = self.constitution//10
        self.piercRes = self.constitution//10
        self.slashRes = self.constitution//10
        self.damage = 1
        self.attRange = 1
        self.armor = (self.strength // 3) + (self.wisdom // 6)
        self.dead = False
        self.action = 0
        self.magicAction = 0
        self.isTurn = False
        self.isMagicTurn = False
        self.targetList = []
        self.target = None
        #set up the creatures AI
        self.ai = aiDict[ai]
        print(self.name + "'s HP: " + str(self.currentHealth))

    def dealDamage(self, target):
        print(self.name + " is attacking " + target.name)
        damage = self.damage + self.strength//2
        self.target.takeDamage(int(damage))
        #return damage formula currently just a basic debug formula

    def takeDamage(self, damage):
        damage = damage - self.armor
        if damage < 1:
            damage = 1
        print(self.name + " is defending")
        self.currentHealth -= int(damage)
        print(self.name + "'s HP: " + str(self.currentHealth))
        #subtract apply damage after applying armor value, currently a debug formula

    def checkDeath(self):
        if self.currentHealth <= 0:
            self.dead = True

    def checkProximity(self, creatureList):#checks if the player is within 1 sqaure of another monster, used during moving or to target melee attacks
        self.proximityList = [None, None, None, None]
        for creatures in creatureList[:]:
            if creatures.positionX == self.positionX and creatures.positionY == self.positionY - 1:
                self.proximityList[0] = creatures
            elif creatures.positionX == self.positionX and creatures.positionY == self.positionY + 1:
                self.proximityList[1] = creatures
            elif creatures.positionX == self.positionX - 1 and creatures.positionY == self.positionY:
                self.proximityList[2] = creatures
            elif creatures.positionX == self.positionX + 1 and creatures.positionY == self.positionY:
                self.proximityList[3] = creatures
        #print(self.proximityList)

    def checkWorldCollision(self, world):#checks if the creature is trying to move into a wall###TODO
        pass


class Humanoid(Creature):
    """This class contains creatures such as goblins, orcs, dwarves, elves and of course Humans"""
    def __init__(self, name, positionX, positionY, symbol, color, faction='neutral', strength=5, constitution=5, dexterity=5, agility=5, intelligence=5, wisdom=5, experience=0, gold=0, ai='passive', headArmor=None, shoulderArmor=None, torsoArmor=None, legArmor=None, footArmor=None, weapon=None, shield=None):
        Creature.__init__(self, name, positionX, positionY, symbol, color, faction, strength, constitution, dexterity, agility, intelligence, wisdom, experience, gold, ai)
        self.headArmor = headArmor
        #print(headArmor)
        self.shoulderArmor = shoulderArmor
        self.torsoArmor = torsoArmor
        self.legArmor = legArmor
        self.footArmor = footArmor
        self.weapon = weapon
        self.shield = shield

        #self.calculateArmor()

    def dealDamage(self, target):
        print(self.name + " is attacking " + target.name)
        self.calculateDamage()
        self.target.takeDamage(int(self.damage))
        #return damage formula currently just a basic debug formula

    def takeDamage(self, damage):
        self.calculateArmor()
        damage -= self.armor
        if damage < 1:
            damage = 1
        print(self.name + " is defending")
        
        self.currentHealth -= int(damage)
        print(self.name + "'s HP: " + str(self.currentHealth))
        #subtract apply damage after applying armor value, currently a debug formula

    def calculateDamage(self):
        if self.weapon != None:
            self.damage = int(self.strength//2 + int(self.weapon.damage))
        else:
            self.damage = int(1 + self.strength//2)
    
    def calculateArmor(self):
        equipArmor = 0
        self.armor = (self.strength // 3) + (self.wisdom // 6)# + (int(self.headArmor.armor) + int(self.torsoArmor.armor) + int(self.shoulderArmor.armor) + int(self.legArmor.armor) + int(self.footArmor.armor) + int(self.shield.armor))
        if self.headArmor != None:
            equipArmor += int(self.headArmor.armor)
        if self.torsoArmor != None:
            equipArmor += int(self.torsoArmor.armor)
        if self.legArmor != None:
            equipArmor += int(self.legArmor.armor)
        if self.footArmor != None:
            equipArmor += int(self.footArmor.armor)
        if self.shoulderArmor != None:
            equipArmor += int(self.shoulderArmor.armor)
        if self.shield != None:
            equipArmor += int(self.shield.armor)
        self.armor += (equipArmor / 5)#find the average armor value of the equipment, the shield counts as bonus and will add to armor value


class Beast(Creature):
    """This class contains creatures such as wolves, bears, lions, etc."""
    def __init__(self, name, positionX, positionY, ai):
        Creature.__init__(self, name, positionX, positionY, strength=5, constitution=5, dexterity=5, agility=5, intelligence=5, wisdom=5, experience=0, gold=0, ai='passive')
        #TODO - fill in unique attributes

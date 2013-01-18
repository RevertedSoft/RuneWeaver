''' This module contains the superclass creature, all other monsters and the player, will inherit from this class.'''

class Creature():

    def __init__(self, strength=5, constitution=5, dexterity=5, agility=5, intelligence=5, wisdom=5, experience=0):
        '''Base constructor method for creatures.'''
        self.strength = strength # helps determine the creatures max health, also applies bonuses to the creatures physical damage
        self.constitution = constitution # helps determine the creatures max health, also applies small bonuses to physical damage resistance
        self.dexterity = dexterity # applies bonuses to the creatures evasion
        self.agility = agility # applies bonuses to the creatures speed
        self.intelligence = intelligence # applies bonuses to magic damage, determines the size of the rune pallete
        self.wisdom = wisdom # applies bonuses to armor and magic resistance, also helps determine the creatures speed with magic
        self.experience = experience #this attribute works 2 ways, it represents the players current experience, and it represents how much experience a player will gain from killing a monster
        #initialize secondary attributes that are determined from the primary attributes
        self.maxHealth = 10 + (self.constitution + (self.strength / 2))#TODO: this is not right
        self.currentHealth = self.maxHealth
        self.palleteSize = (self.intelligence // 3)#TODO: this is not right
        self.armor = (self.strength // 3) + (self.wisdom // 6)
        self.magicRes = (self.intelligence // 6) + (self.wisdom // 3)
        self.evasion = self.dexterity//2
        self.speed = 10 + (self.agility//2)# speed is used to determine how often the creature can do physical actions
        self.magicSpeed = 10 + (self.wisdom//2)# speed is used to determine how often the creature can do magical actions
        self.crushRes = self.constitution//10
        self.piercRes = self.constitution//10
        self.slashRes = self.constitution//10
        self.dead = False
        self.action = 0# when this value reaches 100 the creature is ready to make a physical action
        self.magicAction = 0# when this value reaches 100 the creature is ready to make a magic action
        self.isTurn = False# is it the creatures physical turn?
        self.isMagicTurn = False# is it the creatures magic turn?

        def dealDamage(self):
            pass
            #return damage formula

        def takeDamage(self, damage):
            pass
            #subtract apply damage after applying armor value

        def checkDeath(self):
            if self.currentHealth <= 0:
                self.dead = True

        def turn(self):
            self.checkDeath
            if self.dead:
                pass
                #handle death of the creature
            if self.action < 100:
                self.action += self.speed
                if self.action > 100:
                    self.action = 100
            if self.magicAction < 100:
                self.magicAction += self.magicSpeed
                if self.magicAction > 100:
                    self.magicAction = 100

            

class Humanoid(Creature):
    '''This class contains creatures such as goblins, orcs, dwarves, elves and of course Humans'''
    def __init__(self):
        Creature.__init__()
        self.headArmor = None
        self.shoulderArmor = None
        self.torsoArmor = None
        self.legArmor = None
        self.footArmor = None
        

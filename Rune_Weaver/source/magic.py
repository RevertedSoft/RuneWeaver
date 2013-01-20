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

'''This module contains the rune class.'''

class Rune():
    '''attributes go in order of str, con, dex, agi, int and wis.
Elements go in order of shadow, light, fire, water, wind, earth.'''
    
    def __init__(self, power=0, attriList, elemeList, priority='augment'):#attriList is the list of attributes the rune is affected by. elemeList is the base elements of the rune.
        self.power = power #this determines how powerful this rune is. Affects the damage it may deal, how much it may heal, or how strong a shield it will produce.
        self.strAttune = attriList[0] #these attunement values determine how much their associated attribute affects the strength of the spell
        self.conAttune = attriList[1]
        self.dexAttune = attriList[2]
        self.agiAttune = attriList[3]
        self.intAttune = attriList[4]
        self.wisAttune = attriList[5]
        self.shaAttune = elemeList[0]
        self.ligAttune = elemeList[1]
        self.firAttune = elemeList[2]
        self.watAttune = elemeList[3]
        self.winAttune = elemeList[4]
        self.earAttune = elemeList[5]
        self.priority = priority #this is used alongside the rest of the runes on a pallete to determine what kind of spell will be cast.

class AugmentRune(Rune):
    '''These runes, when added to a spell in the pallete, affect the strength of a spell indirectly.
Augment elements go in order of shadow light fire water wind earth'''
    def __init__(self, power=0, augList):
        Rune.__init__(self, power, [0,0,0,0,0,0], [0,0,0,0,0,0])
        self.shadowAug = augList[0] #these augment values determine how much a spells elements are augmented
        self.lightAug = augList[1]
        self.fireAug = augList[2]
        self.waterAug = augList[3]
        self.windAug = augList[4]
        self.earthAug = augList[5]


class Spell():

    def __init__(self, runeList, caster):
        self.runeList = runeList
        self.caster = caster #the creature casting the spell

        self.castRunes()

        
    def findPriority(self):
        self.priority = 'augment'
        for runes in self.runeList:
            if runes.priority == 'shielding':
                self.priority = 'shielding'
                return
            if runes.priority == 'curse':
                self.priority = 'curse'
            if runes.priority == 'support' and self.priority not 'curse':
                self.priority = 'support'
            if runes.priority == 'combat' and (self.priority not 'support' or self.priority not 'curse'):
                self.priority = 'combat'

    def calcAttunement(self):
        '''This method calculates the most prominent element in the spell. This method will also be used to combine certain elements later.'''
        for runes in self.runeList:
            self.strAttune += runes.strAttune
            self.conAttune += runes.conAttune
            self.dexAttune += runes.dexAttune
            self.agiAttune += runes.agiAttune
            self.intAttune += runes.intAttune
            
            self.shaAttune += runes.shaAttune
            self.ligAttune += runes.ligAttune
            self.firAttune += runes.firAttune
            self.watAttune += runes.watAttune
            self.winAttune += runes.winAttune
            self.earAttune += runes.earAttune

    def augAttunement(self):

        for runes in self.runeList:
            if runes.priority == 'augment':
                self.shaAttune += self.shaAttune * runes.shadowAug
                self.ligAttune += self.shaAttune * runes.lightAug
                self.firAttune += self.shaAttune * runes.fireAug
                self.watAttune += self.shaAttune * runes.waterAug
                self.winAttune += self.shaAttune * runes.windAug
                self.earAttune += self.shaAttune * runes.earthAug

    def calcRange(self):
        
        self.range = 3

        self.range += self.ligAttune//2
        self.range += self.winAttune//2
        self.range -= self.watAttune//3
        self.range -= self.earAttune//3

        

    def castRunes(self):
        '''This method is used when a creature is casting a spell.'''
        self.spellType = self.findPriority() #used to determine the type of spell being cast
        self.calcAttunement() #calculate the attunement values of the spell
        self.augAttunement() #augment the attunements if there are any augment runes
        self.calcRange() #calculate the range of the spell
        self.spellTarget = self.caster.target #determines what creature the spell will effect
    
    






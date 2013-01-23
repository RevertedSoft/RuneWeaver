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

import os

"""This module contains the rune class."""


class Rune():
    """attributes go in order of str, con, dex, agi, int and wis.
    Elements go in order of shadow, light, fire, water, wind, earth.

    power -- describes how powerful a rune is (default 0)
    priority -- is used alongside the rest of the runes on a pallete to determine what kind of spell will be cast (default 'augment')
    name -- the name that the rune is reffered to
    sign -- the sign that is used for the rune, usually a single lowercase or uppercase letter
    attune -- determine how much their associated attribute affects the strength of the spell
    elemeList -- is the base elements of the rune
    attriList -- is the list of attributes the rune is affected by

    """
    def __init__(self, attriList, elemeList, name, sign, power=0, priority='augment'):
        self.power = power
        self.priority = priority
        self.name = name
        self.sign = sign
        #attribute attunements
        self.strAttune = attriList[0]
        self.conAttune = attriList[1]
        self.dexAttune = attriList[2]
        self.agiAttune = attriList[3]
        self.intAttune = attriList[4]
        self.wisAttune = attriList[5]
        #element attunements
        self.shaAttune = elemeList[0]
        self.ligAttune = elemeList[1]
        self.firAttune = elemeList[2]
        self.watAttune = elemeList[3]
        self.winAttune = elemeList[4]
        self.earAttune = elemeList[5]


class AugmentRune(Rune):
    """These runes, when added to a spell in the pallete, affect the strength of a spell indirectly.
    Augment elements go in order of shadow light fire water wind earth

    augment -- determines how much a spells elements are augmented

    """
    def __init__(self, name, sign, augList):
        Rune.__init__(self, [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], name, sign)
        self.shadowAug = augList[0]
        self.lightAug = augList[1]
        self.fireAug = augList[2]
        self.waterAug = augList[3]
        self.windAug = augList[4]
        self.earthAug = augList[5]


class Spell():
    """This class handles spells.

    attributes:
        runeList -- is the list of runes
        caster -- is the creature casting the spell

    methods:
        findPriority -- is used to find the augmentation
        calcAttunement -- calculates the most prominent element in the spell
        augAttunement -- augments the elemental values of the spell using the attributes from augment runes
        calcRange -- calculates casting range
        castRunes -- handles the complete casting of a rune

    """
    def __init__(self, runeList, caster):
        self.runeList = runeList
        self.caster = caster
        self.castRunes()

    def findPriority(self):
        """This method finds out which priority to use for spellcasting. """
        self.priority = 'augment'
        for runes in self.runeList:
            if runes.priority == 'shielding':
                self.priority = 'shielding'
                return  # this returns instantly since shielding is of highest priority. So when shielding is found, it does not need to check anything else.
            if runes.priority == 'curse':
                self.priority = 'curse'
            if runes.priority == 'support' and self.priority != 'curse': # thanks
                self.priority = 'support'
            if runes.priority == 'combat' and (self.priority != 'support' or self.priority != 'curse'):
                self.priority = 'combat'

    def calcAttunement(self):
        """This method calculates the most prominent element in the spell. This method will also be used to combine certain elements later."""
        for runes in self.runeList:
            #attribute attunements
            self.strAttune += runes.strAttune
            self.conAttune += runes.conAttune
            self.dexAttune += runes.dexAttune
            self.agiAttune += runes.agiAttune
            self.intAttune += runes.intAttune
            #element attunements
            self.shaAttune += runes.shaAttune
            self.ligAttune += runes.ligAttune
            self.firAttune += runes.firAttune
            self.watAttune += runes.watAttune
            self.winAttune += runes.winAttune
            self.earAttune += runes.earAttune

    def augAttunement(self):
        """This method augments the elemental attunements. """
        for runes in self.runeList:
            if runes.priority == 'augment':
                self.shaAttune += self.shaAttune * runes.shadowAug
                self.ligAttune += self.shaAttune * runes.lightAug
                self.firAttune += self.shaAttune * runes.fireAug
                self.watAttune += self.shaAttune * runes.waterAug
                self.winAttune += self.shaAttune * runes.windAug
                self.earAttune += self.shaAttune * runes.earthAug

    def calcRange(self):
        """This method calculates the casting range of the spell. """
        self.range = 3

        self.range += self.ligAttune // 2
        self.range += self.winAttune // 2
        self.range -= self.watAttune // 3
        self.range -= self.earAttune // 3

    def castRunes(self):
        """This method is used when a creature is casting a spell.

        It will first determine the type of the spell and then calculate its
        attunement and augements them. After that the casting range is
        calculated and cast upon the caster's target.

        """
        self.spellType = self.findPriority()
        self.calcAttunement()
        self.augAttunement()
        self.calcRange()
        self.spellTarget = self.caster.target



''' The following are functions for making lists of rune objects. '''
def getRunes(directory, file):
    runeList = []
    
    i = 0
    # read the rune text file in the resource directory
    print('Reading rune files.')
    readFile = open(os.path.join(directory,file), "rt")
    while True:
        readLine = readFile.readline()
        if not readLine:
            break
        if '//' in readLine:
            continue
        readLine = readLine[:-1]
        strAtt, conAtt, dexAtt, agiAtt, intAtt, wisAtt, shaAtt, ligAtt, firAtt, watAtt, winAtt, earAtt, name, sign, power, priority  = readLine.split(",")#TODO need to account for any spaces before the name and sign in the text doc
        newRune = Rune( [strAtt, conAtt, dexAtt, agiAtt, intAtt, wisAtt] , [shaAtt, ligAtt, firAtt, watAtt, winAtt, earAtt] ,name, sign, power, priority)

        runeList.append(newRune)

        i += 1

    readFile.close
        

    return runeList

def getAugRunes(directory, file):
    runeList = []
    
    i = 0
    # read the rune text file in the resource directory
    print('Reading rune files.')
    readFile = open(os.path.join(directory,file), "rt")
    while True:
        readLine = readFile.readline()
        if not readLine:
            break
        if '//' in readLine:
            continue
        readLine = readLine[:-1]
        name, sign, shaAug, ligAug, firAug, watAug, winAug, earAug  = readLine.split(",")#TODO need to account for any spaces before the name and sign in the text doc
        newRune = AugmentRune( name, sign , [shaAug, ligAug, firAug, watAug, winAug, earAug] )

        runeList.append(newRune)

        i += 1

    readFile.close
        

    return runeList

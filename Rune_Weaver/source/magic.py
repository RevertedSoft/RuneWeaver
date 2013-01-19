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
Elements go in order of sha, lig, fir, wat, win, ear.'''
    
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
        Rune.__init__(self, power)
        self.shadowAug = augList[0] #these augment values determine how much a spells elements are augmented
        self.lightAug = augList[1]
        self.fireAug = augList[2]
        self.waterAug = augList[3]
        self.windAug = augList[4]
        self.earthAug = augList[5]



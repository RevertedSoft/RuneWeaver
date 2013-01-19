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
    
    def __init__(self, power=0, strAttune=0, conAttune=0, dexAttune=0, agiAttune=0, intAttune=0, wisAttune=0):
        self.power = power #this determines how powerful this rune is. Affects the damage it may deal, how much it may heal, or how strong a shield it will produce.
        self.strAttune = strAttune #these attunement values determine how much their associated attribute affects the strenght of the spell
        self.conAttune = conAttune
        self.dexAttune = dexAttune
        self.agiAttune = agiAttune
        self.intAttune = intAttune
        self.wisAttune = wisAttune

class AugmentRune(Rune):
    '''These runes, when added to a spell in the pallete, affect the strength of a spell indirectly.'''
    def __init__(self, power=0, shadowAug=0, lightAug=0, fireAug=0, waterAug=0, windAug=0, earthAug=0):
        Rune.__init__(self, power)
        self.shadowAug = shadowAug #these augment values determine how much a spells elements are augmented
        self.lightAug = lightAug
        self.fireAug = fireAug
        self.waterAug = waterAug
        self.windAug = windAug
        self.earthAug = earthAug

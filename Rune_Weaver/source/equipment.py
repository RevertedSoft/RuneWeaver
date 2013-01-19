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

'''This module will contain the armor and weapon classes.'''

class Equipment():

    def __init__(self, weight=0, value=0):
        self.weight = weight
        self.value = value

class Weapon(Equipment):

    def __init__(self, weight=0, value=0, damage=1, damType='crushing'):
        Equipment.__init__(self, weight, value)
        
        self.damage = damage
        self.damType = damType

class MagicWeapon(Weapon):

    def __init__(self, weight=0, value=0, damage=1, damType='crushing', runeList=[]):
        Weapon.__init__(self, weight, value, damage, damType)

        self.runes = runeList


class Armor(Equipment):

    def __init__(self, weight=0, value=0, armor=1, crushRes=0, piercRes=0, slashRes=0, bodyLoc='torso'):
        Equipment.__init__(self, weight, value)

        self.armor = armor
        self.crushRes = crushRes
        self.piercRes = piercRes
        self.slashRes = slashRes
        self.bodyLoc = bodyLoc#this is which part of the body the armor can be equiped on

class Shield(Armor):

    def __init__(self, weight=0, value=0, armor=1, crushRes=0, piercRes=0, slashRes=0, bodyLoc='shield', evadeBonus=0):
        Armor.__init__(self, weight, value, armor, crushRes, piercRes, slashRes, bodyLoc)

        self.evadeBonus = evadeBonus

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

"""This module will contain the armor and weapon classes."""


class Equipment():
    """This class handles all equipment items.

    weight -- defines the weight of an equipment item (default 0)
    value -- defines the value of an equipment item (default 0)

    """
    def __init__(self, weight=0, value=0):
        self.weight = weight
        self.value = value


class Weapon(Equipment):
    """This subclass of Equipment handles physical weapons.

    damage -- is the damage of the weapon (default 1)
    damType -- is the type of damage a weapon deals (default 'crushing')
    attRange -- is the attack range of the weapon (default 1)

    """
    def __init__(self, weight=0, value=0, damage=1, damType='crushing', attRange=1):
        Equipment.__init__(self, weight, value)

        self.damage = damage
        self.damType = damType
        self.attRange = attRange


class MagicWeapon(Weapon):
    """This subclass of Weapon handles magical weapons.

    runes -- list of runes available (default [])

    """
    def __init__(self, weight=0, value=0, damage=1, damType='crushing', attRange=1, runeList=[]):
        Weapon.__init__(self, weight, value, damage, damType, attRange)

        self.runes = runeList


class Armor(Equipment):
    """This subclass of Equipment handles armors.

    armor -- is the armor value of an armor piece (default 1)
    crushRes -- is the crush resistance for the damage type crushing
    piercRes -- is the pierce resistance for the damage type piercing
    slashRes -- is the slash resistance for the damage type slashing
    bodyLoc -- defines which body part can wear the armor (default torso)

    """
    def __init__(self, weight=0, value=0, armor=1, crushRes=0, piercRes=0, slashRes=0, bodyLoc='torso'):
        Equipment.__init__(self, weight, value)

        self.armor = armor
        self.crushRes = crushRes
        self.piercRes = piercRes
        self.slashRes = slashRes
        self.bodyLoc = bodyLoc


class Shield(Armor):
    """This subclass of Armor handles all shields.

    evadeBonus -- defins an evade bonus for the wearer (default 0)

    """
    def __init__(self, weight=0, value=0, armor=1, crushRes=0, piercRes=0, slashRes=0, bodyLoc='shield', evadeBonus=0):
        Armor.__init__(self, weight, value, armor, crushRes, piercRes, slashRes, bodyLoc)

        self.evadeBonus = evadeBonus

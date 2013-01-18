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


class Armor(Equipment):

    def __init__(self, weight=0, value=0, armor=1, crushRes=0, piercRes=0, slashRes=0, bodyLoc='torso'):
        Equipment.__init__(self, weight, value)

        self.armor = armor
        self.crushRes = crushRes
        self.piercRes = piercRes
        self.slashRes = slashRes
        self.bodyLoc = bodyLoc#this is which part of the body the armor can be equiped on

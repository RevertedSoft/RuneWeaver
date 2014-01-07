from . import magic, equipment
from .world import *
import os, pygame
from pygame.locals import *

#setup runes and equipment
COMBATRUNELIST = magic.getRunes('resources' + os.sep + 'magic' + os.sep + 'runes', 'combat_runes.txt')
AUGMENTRUNELIST = magic.getAugRunes('resources' + os.sep + 'magic' + os.sep + 'runes', 'augment_runes.txt')
WEAPONLIST = equipment.getWeapons('resources' + os.sep + 'equipment' + os.sep + 'weapons', 'normal_weapons.txt')
MAGICWEAPONLIST = equipment.getMagWeapons('resources' + os.sep + 'equipment' + os.sep + 'weapons', 'magic_weapons.txt')
ARMORLIST = equipment.getArmor('resources' + os.sep + 'equipment' + os.sep + 'armor', 'armor.txt')
SHIELDLIST = equipment.getShields('resources' + os.sep + 'equipment' + os.sep + 'armor', 'shield.txt')

# Colours used while printing to the window
BLUE = (0, 0, 128)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLACK = (0,0,0)
RED = (255,0,0)

#create global world variables from World object
dungeon = []
floor = 0
dungeon.append(World(40, 40))



from . import magic, equipment
import os


COMBATRUNELIST = magic.getRunes('resources' + os.sep + 'magic' + os.sep + 'runes', 'combat_runes.txt')
AUGMENTRUNELIST = magic.getAugRunes('resources' + os.sep + 'magic' + os.sep + 'runes', 'augment_runes.txt')
WEAPONLIST = equipment.getWeapons('resources' + os.sep + 'equipment' + os.sep + 'weapons', 'normal_weapons.txt')
# Colours used while printing to the window
BLUE = (0, 0, 128)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLACK = (0,0,0)
RED = (255,0,0)

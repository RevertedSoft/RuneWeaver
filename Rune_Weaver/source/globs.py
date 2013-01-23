''' This module contains global variables. '''

import os
from . import magic, equipment

COMBATRUNELIST = magic.getRunes('resources' + os.sep + 'magic' + os.sep + 'runes', 'combat_runes.txt')
AUGMENTRUNELIST = magic.getAugRunes('resources' + os.sep + 'magic' + os.sep + 'runes', 'augment_runes.txt')

WEAPONLIST = equipment.getWeapons('resources' + os.sep + 'equipment' + os.sep + 'weapons', 'normal_weapons.txt')

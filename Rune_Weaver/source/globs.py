''' This module contains global variables. '''

import os
from . import magic

COMBATRUNELIST = magic.getRunes('resources' + os.sep + 'magic' + os.sep + 'runes', 'combat_runes.txt')
AUGMENTRUNELIST = magic.getAugRunes('resources' + os.sep + 'magic' + os.sep + 'runes', 'augment_runes.txt')

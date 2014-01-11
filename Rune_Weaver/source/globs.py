from . import magic, equipment, faction, ui, pygcurse#, creature
from .world import *
import os, pygame
from pygame.locals import *

#setup runes and equipment
COMBATRUNELIST = magic.getRunes('resources' + os.sep + 'magic' + os.sep + 'runes', 'combat_runes.txt')
AUGMENTRUNELIST = magic.getAugRunes('resources' + os.sep + 'magic' + os.sep + 'runes', 'augment_runes.txt')
WEAPONLIST = equipment.getWeapons('resources' + os.sep + 'equipment' + os.sep + 'weapons', 'normal_weapons.txt')
#MAGICWEAPONLIST = equipment.getMagWeapons('resources' + os.sep + 'equipment' + os.sep + 'weapons', 'magic_weapons.txt')
ARMORLIST = equipment.getArmor('resources' + os.sep + 'equipment' + os.sep + 'armor', 'armor.txt')
SHIELDLIST = equipment.getShields('resources' + os.sep + 'equipment' + os.sep + 'armor', 'shield.txt')

# Colours used while printing to the window
BLUE = (0, 0, 128)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLACK = (0,0,0)
RED = (255,0,0)
WHITE = (255,255,255)

#create pygcurse window
win = pygcurse.PygcurseWindow(60, 50, 'dungeons')
win.autowindowupdate = False
win.autoupdate = False

#create global world variables from World object
#dungeon = []
#floor = 0
dungeon = World(40, 40)


#create global factions using the Faction object
monsterFaction1 = faction.Faction('monsters', 'aggressive')
playerFaction = faction.Faction('player', 'passive')
monsterFaction2 = faction.Faction('goblins', 'aggressive')

#now create a global faction dict
factionDict = {monsterFaction1.name: monsterFaction1,
               monsterFaction2.name: monsterFaction2,
               playerFaction.name: playerFaction}

#setup dynamic display
eventLog = ui.DynamicDisplay((0,40), (60,10), win, ["Hello"], True, (128,128,128))







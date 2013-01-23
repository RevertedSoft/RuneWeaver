''' This module contains global variables. '''

import os
from . import magic

def getRunes(directory, file):
    runeList = []
    
    i = 0
    # read the rune text file in the resource directory
    print('Reading rune files.')
    readFile = open(os.path.join(directory,file), "rt")
    while True:
        readLine = readFile.readline()
        if not readLine:
            break
        if '//' in readLine:
            continue
        readLine = readLine[:-1]
        strAtt, conAtt, dexAtt, agiAtt, intAtt, wisAtt, shaAtt, ligAtt, firAtt, watAtt, winAtt, earAtt, name, sign, power, priority  = readLine.split(",")#TODO need to account for any spaces before the name and sign in the text doc
        newRune = magic.Rune( [strAtt, conAtt, dexAtt, agiAtt, intAtt, wisAtt] , [shaAtt, ligAtt, firAtt, watAtt, winAtt, earAtt] ,name, sign, power, priority)

        runeList.append(newRune)

        i += 1

    readFile.close
        

    return runeList

def getAugRunes(directory, file):
    runeList = []
    
    i = 0
    # read the rune text file in the resource directory
    print('Reading rune files.')
    readFile = open(os.path.join(directory,file), "rt")
    while True:
        readLine = readFile.readline()
        if not readLine:
            break
        if '//' in readLine:
            continue
        readLine = readLine[:-1]
        name, sign, shaAug, ligAug, firAug, watAug, winAug, earAug  = readLine.split(",")#TODO need to account for any spaces before the name and sign in the text doc
        newRune = magic.AugmentRune( name, sign , [shaAug, ligAug, firAug, watAug, winAug, earAug] )

        runeList.append(newRune)

        i += 1

    readFile.close
        

    return runeList

COMBATRUNELIST = getRunes('resources' + os.sep + 'magic' + os.sep + 'runes', 'combat_runes.txt')
AUGMENTRUNELIST = getAugRunes('resources' + os.sep + 'magic' + os.sep + 'runes', 'augment_runes.txt')

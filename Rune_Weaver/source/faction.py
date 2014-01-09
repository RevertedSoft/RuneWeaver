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

class Faction():

    def __init__(self, name, behavior):
        """The Faction class represents the larger enteties of the game world, each faction has its own relation with the other factions and its own behavior towards
           meeting other factions. Eventually the behavior of a faction should affect the ai of the creatures within the faction.

           attributes:
               behaviorDict --- determines which behavior the faction will use, this is obtained through the behavior argument in the init call
               name --- the name of the faction
               behavior --- see above
               knownFactionDict --- a dictionary of all the known factions
               factionRelationDict --- a dictionary of the relations towards the given factions"""
        
        self.behaviorDict = {'friendly':self.behaviorFriendly,
                             'passive':self.behaviorPassive,
                             'aggressive':self.behaviorAggressive}
        self.name = name
        self.behavior = self.behaviorDict[behavior]#this will determine whether a faction is hostile towards other factions upon meeting them, or friendly
        self.knownFactionDict = {}
        self.factionRelationDict = {}


    def meetNewFaction(self, faction):
        factionName = faction.name
        self.knownFactionDict[factionName] = faction
        self.behavior(self.knownFactionDict[factionName])
        #this method is used when one faction is meeting another for the first time


    def setRelation(self, faction, value):
        #used to set initial relations of a faction
        self.factionRelationDict[faction] = value

    def alterRelation(self, faction, value):
        self.factionRelationDict[faction] += value


    def behaviorFriendly(self, faction):
        self.setRelation(faction.name, 20)


    def behaviorPassive(self, faction):
        
        pass


    def behaviorAggressive(self, faction):
        self.alterRelation(faction, -20)



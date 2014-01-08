#module will contain the faction class used by all entities in the game





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
        #pass


    def setRelation(self, faction, value):
        self.factionRelationDict[faction] = value

    def alterRelation(self, faction, value):
        self.factionRelationDict[faction] += value


    def behaviorFriendly(self, faction):
        self.setRelation(faction.name, 20)
        #pass


    def behaviorPassive(self, faction):
        
        pass


    def behaviorAggressive(self, faction):
        self.alterRelation(faction, -20)
        #pass



##newFaction1 = Faction('default', 'friendly', {})
##newFaction2 = Faction('hostile', 'aggressive', {})
##
##newFaction1.meetNewFaction(newFaction2)
##
##print(newFaction1.knownFactionDict)
##print(newFaction1.factionRelationDict)
##newFaction1.alterRelation('hostile', -40)
##print(newFaction1.factionRelationDict)
##
##print(newFaction1.name)

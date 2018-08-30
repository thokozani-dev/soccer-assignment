
from teamscore import TeamScore
from teamranking import TeamRanking

class TeamRankingTable:
    
    __uniqueTeamNames   = []
    __teamRankings      = []
    
    # Gets unique team names list based on results only (since we do not use a database)
    def buildUniqueTeamNames( self, teamsCollection = [] ):
        
        if len( teamsCollection ) > 0:
            for team in teamsCollection:
                if isinstance( team, TeamScore):
                    # only process TeanScore instances
                    if team.getTeamName() not in self.__uniqueTeamNames:
                        # Team does not exist in the unique names collection. So add it
                        self.__uniqueTeamNames.append( team.getTeamName() )
    
    
    def getUniqueTeamNames( self ):
        return self.__uniqueTeamNames
    
    
    def buildDefaultRankingsTableFromTeamNames( self, uniqueTeamNames = [] ):
        for teamName in uniqueTeamNames:
            if self.findTeamInRankingList( teamName ) == None:
                self.__teamRankings.append( TeamRanking( teamName, 0 ) )
    
    
    def getTeamRankingsTable( self ):
        # Sort by lambda using the points first
        self.__teamRankings.sort( key=lambda team: team.getTeamPoints(), reverse=True )
        return self.__teamRankings
    
    
    def findTeamInRankingList( self, subjectTeamName = None ):
        if subjectTeamName != None:
            for team in self.__teamRankings:
                if team.getTeamName().lower() == subjectTeamName.lower():
                    return team
                
        return None # otherwise return nothing
    
    
    # Adds points to a team.
    def addPointsToTeam( self, subjectTeamName = None, points = 0 ):
        team    = self.findTeamInRankingList( subjectTeamName )
        
        # Aggregate the points if the object is not "None"
        if team != None:
            team.setTeamPoints( team.getTeamPoints() + points )
            
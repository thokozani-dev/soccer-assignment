
'''
    This class is responsible for building the team standings / ranks based on 
    match scores. It utilizes other objects like TeamScore and TeamRanking which 
    are in charge of team identity and points
'''

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
    
    
    # Gets unique tables collection
    def getUniqueTeamNames( self ):
        return self.__uniqueTeamNames
    
    
    # Builds the team rankings from unique team names collection
    def buildDefaultRankingsTableFromTeamNames( self, uniqueTeamNames = [] ):
        for teamName in uniqueTeamNames:
            if self.findTeamInRankingList( teamName ) == None:
                self.__teamRankings.append( TeamRanking( teamName, 0 ) )
    
    
    # Gets team rankings collection
    def getTeamRankingsTable( self ):
        # Sort by lambda using the points first
        self.__teamRankings.sort( key=lambda team: team.getTeamPoints(), reverse=True )
        
        # Get a points array
        points  = []
        for teamRanking in self.__teamRankings:
            if teamRanking.getTeamPoints() not in points:
                points.append( teamRanking.getTeamPoints() )
                
        # Assign rank by points for each team. We will use the points array created above
        rank    = 1
        for point in points:
            for teamRanking in self.__teamRankings:
                if teamRanking.getTeamPoints() == point:
                    # Assign the current rank index (variable is "rank" in this case)
                    teamRanking.setTeamRank( rank )
                    
            rank += 1
            
        
        return self.__teamRankings
    
    
    # Get a team in the __teamRankings instance via the supplied name
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
            
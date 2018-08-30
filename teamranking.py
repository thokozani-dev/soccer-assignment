
'''
    TeamRanking is used in TeamRankingTable for calculating the points for a team
'''

class TeamRanking:
    
    __name      = ''
    __points    = 0
    __rank      = 0
        
    # Object constructor with optional parameters
    def __init__( self, name = '',  points = 0, rank = 0 ):
        self.__name     = name
        self.__points   = points
        self.__rank     = rank
        
    
    # Sets the team name of this object
    def setTeamName( self, name = '' ):
        self.__name = name
        
    
    # Gets the team name from this object    
    def getTeamName( self ):
        return self.__name
    
    
    # Sets the team's rank of this object
    def setTeamRank( self, rank = 0 ):
        self.__rank = rank
        
        
    # Gets the team's rank from this object
    def getTeamRank( self ):
        return self.__rank
    
    
    # Sets the team points of this object
    def setTeamPoints( self , points = 0 ):
        self.__points = points
    
    
    # Gets the team total points from this object
    def getTeamPoints( self ):
        return self.__points
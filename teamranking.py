
'''
    TeamRanking is used in TeamRankingTable for calculating the 
'''

class TeamRanking:
    
    __name      = ''
    __points    = 0
        
    
    def __init__( self, name = '',  points = 0 ):
        self.__name     = name
        self.__points   = points
        
    
    # Sets the team name of this object
    def setTeamName( self, name = '' ):
        self.__name = name
        
    
    # Gets the team name from this object    
    def getTeamName( self ):
        return self.__name
    
    
    # Sets the team points of this object
    def setTeamPoints( self , points = 0 ):
        self.__points = points
    
    
    # Gets the team total points from this object
    def getTeamPoints( self ):
        return self.__points
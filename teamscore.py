
'''
    This class will be used to represent teams from the data source.
'''

class TeamScore:
    
    __name      = ''    # The name of the team
    __score     = 0     # The amount the team has scored
    
    
    # Object constructor with optional parameters
    def __init__( self, name = '', score = 0 ):
        self.__name     = name
        self.__score    = score
        
    
    # Mutates the team name attribute for this object
    def setTeamName( self, name ):
        self.__name = name
        
        
    # Mutates the team score attribute for this object
    def setTeamScore( self, score ): 
        self.__score = score
        
        
    # Retrieves team name attribute from this object
    def getTeamName( self ):
        return self.__name
    
    
    # Retrieves team score attribute from this object
    def getTeamScore( self ):
        return self.__score
    
    
    # Creates a string of attribute of this object
    def toString( self ):
        return self.__name + ' with ' + str( self.__score ) + ' goal(s)'
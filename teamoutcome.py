
'''
    TeamOutcome is just a utility class that utilizes TeamScore to determine the winner 
    between the two competing teams. This will probably be listed in a "util" class but for 
    simplicity sake we kept it in the root folder
'''

from teamscore import TeamScore

class TeamOutcome:
    
    __teamOne   = TeamScore()
    __teamTwo   = TeamScore();
    
    
    # Object constructor with optional parameters
    def __init__( self, teamOne = TeamScore(), teamTwo = TeamScore() ):
        self.__teamOne  = teamOne
        self.__teamTwo  = teamTwo
    
        
    # Determines if theres a winner between the two teams
    def hasWinner( self ):
        if self.__teamOne.getTeamScore() > self.__teamTwo.getTeamScore():
            return True
        elif self.__teamTwo.getTeamScore() > self.__teamOne.getTeamScore():
            return True
        
        return False
    
    
    # Get the winner between the 2 teams
    def getWinner( self ):
        if self.__teamOne.getTeamScore() > self.__teamTwo.getTeamScore():
            return self.__teamOne
        elif self.__teamTwo.getTeamScore() > self.__teamOne.getTeamScore():
            return self.__teamTwo
        else:
            return None
from teamscore import TeamScore
from teamoutcome import TeamOutcome
from teamrankingtable import TeamRankingTable

from os import path
        
# Iterating through each line and create teams
def printRankings( filePath = None, testMode = False ):
    
    # If the file path is not provided you will be prompted for it
    if filePath == None:
        filePath    = raw_input( 'Please enter the file path containing scores in your computer: ' )
        
    # Formatting slashes
    filePath    = str( filePath ).replace( '\\', '/' )

    # \Users\refreshdevelopment\Documents\scores.txt
    # \Users\refreshdevelopment\Documents\out-scores.txt
    # \Users\refreshdevelopment\Documents\empty.txt
    
    # Array for reading the file line by line
    lines   = []
    
    if path.exists( filePath ):
    
        with open( filePath, "r" ) as file:
            for line in file:
                line = line.rstrip( '\n' ) # Remove any line breaks
                lines.append( line )
            
        # Instantiating the rankings object
        rankingTable = TeamRankingTable();
        
        if len( lines ) <= 0:
            if testMode == False:
                print( 'Could not produce a rankings table with the specified file. It could be empty. Try again' )
                printRankings()
            else:
                return 'Could not produce a rankings table with the specified file. It could be empty. Try again'
                
        else:
            for line in lines:
                teamEntities    = line.split( ',' )
                teams           = []
                
                if len( teamEntities ) > 0:
                    for team in teamEntities:
                        teamAndScoreEntities    = team.split( ' ' )
                        
                        # clean empty spaces. had to wrap this in list() for array type after filter(...)
                        teamAndScoreEntities    = list( filter( None, teamAndScoreEntities ) )
                        
                        # Based on input, scores are at the end of the array
                        score   = teamAndScoreEntities[ len( teamAndScoreEntities ) - 1 ]
                        teamAndScoreEntities.pop();
                        
                        team    = ' '.join( teamAndScoreEntities )
                         
                        # Create the TeamScore and add to the teams array
                        teams.append( TeamScore( team, int( score ) ) )
                        
                        rankingTable.buildUniqueTeamNames( teams )
                
                
                # Once the unique names have been determined, each name will have a 0 assigned to it
                # using the function below.
                rankingTable.buildDefaultRankingsTableFromTeamNames( rankingTable.getUniqueTeamNames() )
                
                '''
                    teams[] array should have [ TeamScore, TeamScore ] in the collection.
                    Exactly 2 items in. No more, no less
                '''
                
                # TeamOutcome object determines who is the winner of the 2 teams
                outcome     = TeamOutcome( teams[0], teams[1] )
                hasWinner   = outcome.hasWinner()
                
                if hasWinner:
                    # Add 3 points to the rankings table using the team name
                    rankingTable.addPointsToTeam( outcome.getWinner().getTeamName() , 3 )
                else:
                    # Add 1 point to each team using their names
                    rankingTable.addPointsToTeam( teams[0].getTeamName(), 1 )
                    rankingTable.addPointsToTeam( teams[1].getTeamName(), 1 )
                    
            
            # Print the rankings table. If in test mode return the string instead
            rankings    = rankingTable.getTeamRankingsTable()
            if len( rankings ) > 0:
                index       = 1
                testString  = ''
                for rank in rankings:
                    if testMode == False:
                        print( str ( index ) + '. ' + rank.getTeamName() + ' ' + str( rank.getTeamPoints() ) + ' pts' )
                    else:
                        testString += str ( index ) + '. ' + rank.getTeamName() + ' ' + str( rank.getTeamPoints() ) + ' pts\n'
                    
                    index += 1
                    
                if testMode == True:
                    return testString.rstrip('\n')
            else:
                
                if testMode == False:
                    print( 'Could not produce a rankings table with the specified file. It could be empty. Try again' )
                    printRankings()
                else:
                    return 'Could not produce a rankings table with the specified file. It could be empty. Try again'
                
    else:
        
        if testMode == False:
            print( 'The file in specified path does not exist. Try again' )
            printRankings()
        else: 
            return 'The file in specified path does not exist. Try again'

        


            
    
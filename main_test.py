'''
This unit test uses local files for testing functionality
'''

from main import printRankings
import re
import unittest

class MainUnitTest( unittest.TestCase ):
    
    __testmode  = True
    
    # This test assumes everything is fine and ranking table can be produced
    def testRankingsFine( self ):
        self.assertEqual( printRankings( 'scores.txt', self.__testmode ), "1. Tarantulas 6 pts\n2. Lions 5 pts\n3. Snakes 1 pts\n3. FC Awesome 1 pts\n4. Grouches 0 pts" )
        
        
    # This test assumes the file cannot be found
    def testRankingsFileNotFound( self ):
        self.assertEqual( printRankings( 'scor.txt', self.__testmode ), "The file in specified path does not exist. Try again" )
        
    
    # This test assumes the file is empty 
    def testRankingsFileEmpty( self ):
        self.assertEqual( printRankings( 'score-empty.txt', self.__testmode ), 'Could not produce a rankings table with the specified file. It could be empty. Try again' )
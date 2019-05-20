import unittest
from app.news import Source 

class SourceTest(unittest.TestCase):
    def test_source(self):
        '''
        test_source checks that new news source objects are created
        '''
        self.new_source = Source('one','two','three','four','five',) 
        self.assertTrue(isinstance(self.new_source,Source))

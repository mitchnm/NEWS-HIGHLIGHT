import unittest
from app.news import Articles

class ArticlesTest(unittest.TestCase):
    def setUp(self):
        '''
        test_source checks that new news source objects are created
        '''
        self.new_article = Articles('one','two','three','four','five')
    
    def test_instance(self):    
        self.assertTrue(isinstance(self.new_article,Articles))


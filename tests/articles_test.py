import unittest
from app.news import Articles, Source 

class ArticlesTest(unittest.TestCase):
    def test_article(self):
        '''
        test_source checks that new news source objects are created
        '''
        self.new_article = Articles('one','two','three','four','five')
        self.assertTrue(isinstance(self.new_article,Articles))


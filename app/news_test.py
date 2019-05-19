import unittest
from .models.news import Articles,Source
class ArticleTest(unittest.TestCase):

    def test_article(self):
        '''
        test_source checks that new news source objects are created
        '''
        self.new_article = Articles('me','bbc-news','Jesus','is alive','eng')
        self.assertTrue(isinstance(self.new_article,Articles))

class SourceTest(unittest.TestCase):

    def test_source(self):
        '''
        test_source checks that new news source objects are created
        '''
        self.new_source = Source('bbc-news','Jesus','is alive','eng','who',)
        self.assertTrue(isinstance(self.new_source,Source))

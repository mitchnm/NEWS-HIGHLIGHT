import unittest
from .models.news import Articles


class ArticleTest(unittest.TestCase):

    '''
    Test Class to test the behaviour of the Source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Articles(' author', 'title', 'desc', 'url', 'image')

    def test_instance(self):
        '''
           This method will test if self.new_article is an object of the article class.
        '''
        self.assertTrue(isinstance(self.new_article, Articles))

if __name__ == '__main__':
    unittest.main()

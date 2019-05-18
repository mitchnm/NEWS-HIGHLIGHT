import unittest
from .models import news
News = news.News

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News(1234,'Python Must Be Crazy','https://image.tmdb.org/t/p/w500/khsjha27hbs','A thrilling new Python Series')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = News('abc-news','ABC News','Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))

if __name__ == '__main__':
    unittest.main()

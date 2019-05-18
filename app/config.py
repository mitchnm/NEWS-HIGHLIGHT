class Config:
    '''
    General configuration parent class
    '''
NEWS_API_BASE_URL ='https://newsapi.org/v2/sources?category=sports&apiKey=7723e3d4015244ffa335f2e75abe5dbb'
ARTICLES_API_BASE_URL = 'https://newsapi.org/v2/top-headlines?language=en&apiKey=7723e3d4015244ffa335f2e75abe5dbb'

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

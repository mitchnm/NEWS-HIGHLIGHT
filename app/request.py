import urllib.request,json
from .news import Source, Articles
 
api_key = None
base_url = None
articles_url = None

def configure_request(app):
    global api_key, base_url, articles_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_SOURCES_BASE_URL']
    articles_url = app.config['NEWS_ARTICLES_BASE_URL']

def get_sources(category):
    '''
    Function that gets the json response to our url request.
    '''
    get_sources_url = 'https://newsapi.org/v2/sources?language=en&category={}&apikey=7723e3d4015244ffa335f2e75abe5dbb'.format(category)
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)
        source_results = None
        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_results(source_results_list)
    return source_results

def process_results(source_list):
    '''
    Function  that processes the source result and transform them to a list of Objects
    Args:
        source_list: A list of dictionaries that contain source details
    Returns :
        source_results: A list of source objects
    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url') 
        category = source_item.get('category')
        source_object = Source(id, name, description, url, category)
        source_results.append(source_object)
    return source_results

def get_articles(id):
    '''
    Function that gets the json response to our articles url request.
    '''
    get_all_articles_url = 'https://newsapi.org/v2/everything?sources={}&apiKey=7723e3d4015244ffa335f2e75abe5dbb'.format(id)
    with urllib.request.urlopen(get_all_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)
        articles_results = None
        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles(articles_results_list)
    return articles_results


def process_articles(articles_list):
    '''
    Function  that processes the articles result and transform them to a list of Objects
    Args:
        articles_list: A list of dictionaries that contain articles details
    Returns :
        articles_results: A list of articles objects
    '''
    articles_results = []
    for articles_item in articles_list:
        title = articles_item.get('title')
        image = articles_item.get('urlToImage')
        description = articles_item.get('description')
        url = articles_item.get('url')
        date = articles_item.get('publishedAt')
        articles_object = Articles(title, image, description, url, date)
        articles_results.append(articles_object)
    return articles_results



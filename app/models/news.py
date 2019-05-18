class News:
    '''
    Movie class to define Movie Objects
    '''

    def __init__(self,id,source,article,image,):
        self.id =id
        self.source = source
        self.article = article
        self.image= 'https://image.tmdb.org/t/p/w500/'+ image
        
class Source:
    '''
    Movie class to define Movie Objects
    '''

    def __init__(self, id, name, description):
        self.id =id
        self.name = name
        self.description = description

class Articles:
    '''
    defines the articles objects
    '''

    def __init__(self, blue, id, title, author, description, urlToImage, publishedAt, url):
        self.blue = blue
        self.title = title
        self.author = author
        self.description = description
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.url = url
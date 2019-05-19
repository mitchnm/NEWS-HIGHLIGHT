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

    def __init__(self, id, name, description, url, category):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category

class Articles:
    '''
    defines the articles objects
    '''

    def __init__(self, title, image, description, url, date):
        self.title = title
        self.image = image
        self.description = description
        self.url = url
        self.date = date
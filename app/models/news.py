class News:
    '''
    Movie class to define Movie Objects
    '''

    def __init__(self,id,source,article,image,):
        self.id =id
        self.source = source
        self.article = article
        self.image= 'https://image.tmdb.org/t/p/w500/'+ image
        
        
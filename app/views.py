from flask import render_template
from app import app
from .request import get_sources, get_articles

@app.route('/')
def index():
  '''
  view the first page
  '''
  title = 'Home'
  science_sources = get_sources('science')
  business_sources = get_sources('business') 
  entertainment_sources = get_sources('entertainment')
  general_sources = get_sources('general')
  health_sources = get_sources('health')
  sports_sources = get_sources('sports')
  technology_sources = get_sources('technology')
  return render_template('index.html',title = title,science=science_sources, business=business_sources, entertainment=entertainment_sources, sports=sports_sources, health=health_sources, general=general_sources, technology=technology_sources) 

@app.route('/articles/<int:id>')
def articles(id):
    '''
    Shows
    '''

    news = get_articles(id)

    title = "Top Headlines"
    return render_template('articles.html', title = title, news = news)
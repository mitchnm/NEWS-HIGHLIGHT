from flask import render_template
from app import app
from .request import get_sources, get_articles

@app.route('/')
def index():
  '''
  view the first page
  '''
  title = 'Home - Welcome to The best Movie Review Website Online'
  return render_template('index.html',title = title) 

@app.route('/articles/<id>')
def articles(id):
    '''
    Shows
    '''

    news = get_articles(id)

    title = "Top Headlines"
    return render_template('articles.html', title = title, news = news)
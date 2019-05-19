from flask import render_template, request, redirect, url_for
from app import app
from .request import get_sources, get_articles

@app.route('/')
def index():
  '''
  view the first page
  '''
  title = 'Home'
  science_sources = get_sources('science')

  return render_template('index.html',title = title, science=science_sources) 

@app.route('/articles/<int:id>')
def articles(id):
    '''
    Shows
    '''

    news = get_articles(id)

    title = "Top Headlines"
    return render_template('articles.html', title = title, news = news)
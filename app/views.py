from flask import render_template
from app import app

@app.route('/')
def index():
  '''
  view the first page
  '''
  title = 'Home - Welcome to The best Movie Review Website Online'
  return render_template('index.html',title = title) 

@app.route('/news/<int:news_id>')
def movie(news_id):

    '''
    View news details
    '''
    return render_template('news.html',id = news_id)

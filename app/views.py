from flask import render_template
from app import app

@app.route('/')
def index():
  '''
  view the first page
  '''
  message = 'NGAMIA WEWE'
  return render_template('index.html',message = 'NGAMIA WEWE') 

@app.route('/news/<int:news_id>')
def movie(news_id):

    '''
    View news details
    '''
    return render_template('news.html',id = news_id)

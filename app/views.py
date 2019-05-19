from flask import render_template, request, redirect, url_for
from app import app
from .request import get_sources, get_articles, search_articles

#Views


@app.route('/')
def index():
    '''
    View root page.
    ''' 

    title = 'Home - NewsApp'

    business_sources = get_sources('business')

    entertainment_sources = get_sources('entertainment')

    general_sources = get_sources('general')

    sports_sources = get_sources('sports')

    technology_sources = get_sources('technology')

    return render_template('index.html', title=title, business=business_sources, entertainment=entertainment_sources, sports=sports_sources, general=general_sources, technology=technology_sources)


@app.route('/source/<id>')
def source(id):
    '''
    View source page.
    '''
    all_articles = get_articles(id)
    title = f'NewsApp -- {id.upper()}'
    id_up = id.upper()

    return render_template('article.html', articles=all_articles, title=title, id_up=id_up)



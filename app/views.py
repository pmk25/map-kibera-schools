# -*- coding: utf-8 -*-
"""
    app.views
    ~~~~~~~~~

    The endpoints and stuff

    :author: Philip Schleihauf
    :copyright: © 2014 by Feedback Labs
    :license: 
"""

from flask import render_template, Markup
from . import app
from .content import blog, data, stories


@app.route('/')
def home():
    # get all the pieces
    return render_template('home.html')


@app.route('/schools/<school_id>')
def school(school_id):
    # get data about this school or 404
    # build the templating context
    return render_template('school-profile.html')


@app.route('/blog/<slug>')
def blog(slug):
    # open file or abort 404
    # run it through markdown
    # build the templating context
    return render_template('blog-post.html')


@app.route('/404.html')
@app.errorhandler(404)
def not_found(err=None):
    """GitHub Pages not-found template."""
    code = 404 if err else 200  # frozen-flask doesn't like not-200 responses
    return render_template('404.html'), code
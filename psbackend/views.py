########## Module with all of our views ##########
from flask import url_for

from psbackend import app
from . import templateutil

@app.route('/')
@app.route('/index')
def index():
    return templateutil.render('index.html')

@app.route('/generic')
def generic():
    return templateutil.render('generic.html')

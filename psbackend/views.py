########## Module with all of our views ##########
from flask import request

from psbackend import app
from . import templateutil

@app.route('/')
@app.route('/index')
def index():
    return templateutil.render('index.html', pageTitle="Home")

@app.route('/about')
def about():
    return templateutil.render('about.html', pageTitle="About")

@app.route('/login', methods=['GET', 'POST'])
def login():
    print(request.form)
    return templateutil.render('login.html', pageTitle="Login")
            #extraJsFiles=["js/login.js"])

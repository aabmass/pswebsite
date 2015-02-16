########## Module with all of our views ##########
from flask import request, flash, redirect, url_for
from flask.ext.login import login_user, current_user, login_required

from . import app
from . import templateutil
from .user import User

@app.route('/')
@app.route('/index')
def index():
    return templateutil.render('index.html', pageTitle="Home")

@app.route('/about')
def about():
    return templateutil.render('about.html', pageTitle="About")

@app.route('/user')
@login_required
def user():
    return templateutil.render('user.html', pageTitle=current_user.get_id())

@app.route('/login', methods=['GET', 'POST'])
def login():
    print(request.form)
    # login and validate the user...
    if request.method == "POST":
        user = User(request.form["email"])
        login_user(user)
        print("Logged in successfully")
        flash("Logged in successfully.")
        return redirect(request.args.get("next") or url_for("index"))

    return templateutil.render('login.html', pageTitle="Login")
            #extraJsFiles=["js/login.js"])

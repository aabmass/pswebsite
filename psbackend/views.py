########## Module with all of our views ##########
from flask import request, flash, redirect, url_for
from flask.ext.login import login_user, current_user, login_required

# For debugging
import pprint

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


@app.route('/createuser', methods=['GET', 'POST'])
def createuser():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        firstName = request.form["firstName"]
        lastName = request.form["lastName"]

        newUser = User(email=email, password=password,
                       firstName=firstName, lastName=lastName)

    return templateutil.render('logincreateuser.html', pageTitle="Create User")


@app.route('/login', methods=['GET', 'POST'])
def login():
    # login and validate the user...
    if request.method == "POST":
        user = User(request.form["email"])
        login_user(user)
        print("Logged in successfully")
        flash("Logged in successfully.")
        return redirect(request.args.get("next") or url_for("index"))

    return templateutil.render('logincreateuser.html', pageTitle="Login")

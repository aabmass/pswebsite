########## Module with all of our views ##########
from flask import request, flash, redirect, url_for
from flask.ext.login import login_user, logout_user, current_user, login_required

from . import app
from . import templateutil
from .models.user import *

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
    if request.method == "GET":
        return templateutil.render('logincreateuser.html', pageTitle="Create User")

    email = request.form["email"]
    password = request.form["password"]
    firstName = request.form["firstName"]
    lastName = request.form["lastName"]

    user = User(email=email, password=password,
            firstName=firstName, lastName=lastName)

    # Make sure validated first...
    user.save()
    login_user(user)
    flash("Logged in successfully.")
    return redirect(request.args.get("next") or url_for("index"))



@app.route('/login', methods=['GET', 'POST'])
def login():
    # login and validate the user...
    if request.method == "GET":
        return templateutil.render('logincreateuser.html', pageTitle="Login")

    user = loadUser(request.form["email"])

    # check to see if the given password hashes right
    # TODO: setup with forms handler
    if user.checkPassword(request.form["password"]):
        login_user(user)
        flash("Logged in successfully.")
        return redirect(request.args.get("next") or url_for("index"))
    else:
        flash("Logged in unsuccessfully.")
        return templateutil.render('logincreateuser.html', pageTitle="Login",
                                    wrongPassword=True)

@app.route('/logout')
def logout():
    # logout the current user
    logout_user()
    flash("Logged out successfully")
    return redirect(request.args.get("next") or url_for("index"))

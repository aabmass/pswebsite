#!/usr/bin/env python3
from psbackend import app
from psbackend.user import User
from psbackend.user import users
from flask.ext.login import LoginManager

app.secret_key = "ROOISMYROOANDDUCKISDUCK"

loginManager = LoginManager()
loginManager.init_app(app)


@loginManager.user_loader
def load_user(userId):
    user = None
    if userId in users.keys():
        user = users[userId]
    return user

app.debug = True
app.run()

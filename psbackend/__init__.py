from flask import Flask
from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy

import os

## Flask init
app = Flask(__name__)



app.secret_key = "ROOISMYROOANDDUCKISDUCK"

## DB Init
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://psflask:{}@localhost/psdev'.format(os.environ["DBPASS"])
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://psflask:{}@localhost/psdev'.format(os.environ["DBPASS"])

db = SQLAlchemy(app)

loginManager = LoginManager()
loginManager.init_app(app)

from .models.user import User

## Application local init

from . import views
from . import context
from . import menus


# Create the menus
menus.createApplicationMenus()

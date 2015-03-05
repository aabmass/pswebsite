from flask import Flask
from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy

import os, sys

try:
    from psbackend import config
except ImportError:
    print("Please create a config.py file in the psbackend directory.\n"
          "Use config.sample.py as a starting point")
    sys.exit(1)

## Flask init
app = Flask(__name__)
app.secret_key = config.secret_key

## DB Init
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'mysql+mysqlconnector://{0.dbuser}:{0.dbpass}@localhost/{0.dbname}'.format(config)

db = SQLAlchemy(app)

loginManager = LoginManager()
loginManager.init_app(app)
loginManager.login_view = "login"

from psbackend.models.user import User

## Application local init

from psbackend.views import *
from psbackend import context
from psbackend import menus


# Create the menus
menus.createApplicationMenus()

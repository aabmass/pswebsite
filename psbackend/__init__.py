from flask import Flask
from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy

## Flask init
app = Flask(__name__)

loginManager = LoginManager()
loginManager.init_app(app)


app.secret_key = "ROOISMYROOANDDUCKISDUCK"

db = SQLAlchemy(app)

## Application local init

from . import views
from . import context
from . import menus


# Create the menus
menus.createApplicationMenus()


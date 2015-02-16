from flask import Flask
from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

from . import views
from . import context
from . import menus

loginManager = LoginManager()
loginManager.init_app(app)


app.secret_key = "ROOISMYROOANDDUCKISDUCK"

db = SQLAlchemy(app)

# Create the menus
menus.createApplicationMenus()


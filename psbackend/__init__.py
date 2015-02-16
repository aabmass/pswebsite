from flask import Flask

app = Flask(__name__)

from . import views
from . import context
from .menus import Menu

# Create the menus
menus = context.projectVars["menus"]
menus.append(Menu("Home", "index"))


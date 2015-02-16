from flask import Flask

app = Flask(__name__)

from . import views
from . import context
from . import menus

# Create the menus
menus.createApplicationMenus()


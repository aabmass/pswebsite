########## Utils for rendering the templates ##########
import flask
from flask.ext.login import current_user

from psbackend import context
from psbackend.menus import UserMenu, Menu

## Use this in place of flask.render_template for the project
def render(templateName, **kwargs):
    return flask.render_template(templateName, projVars=context.projectVars,
                                 **kwargs)

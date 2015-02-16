########## Utils for rendering the templates ##########
import flask
from . import context

## Use this in place of flask.render_template for the project
def render(templateName, **kwargs):
    print("Will call: render_template({}, {})".format(templateName, kwargs))
    return flask.render_template(templateName, projVars=context.projectVars, **kwargs)

from psbackend import app
from psbackend import templateutil

from psbackend import models

@app.route('/')
@app.route('/admin')
def admin():
    return templateutil.render('admin.html', pageTitle="Admin",
        models=allModels())

def allModels():
    """ Returns all model classes """
    classes = []
    for modName in models.all:
        mod = models.__dict__[modName]
        classes.append(mod.__dict__[modName.capitalize()])
    return classes

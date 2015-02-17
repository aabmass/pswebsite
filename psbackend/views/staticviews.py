from psbackend import app
from psbackend import templateutil

from flask.ext.login import current_user, login_required

@app.route('/')
@app.route('/index')
def index():
    return templateutil.render('index.html', pageTitle="Home")

@app.route('/about')
def about():
    return templateutil.render('about.html', pageTitle="About")

@app.route('/user')
@login_required
def user():
    return templateutil.render('user.html', pageTitle=current_user.get_id())

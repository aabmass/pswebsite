########## Module with all of our views ##########
from psbackend import templateutil
from psbackend import app

@app.route('/')
@app.route('/index.html')
def index():
    return templateutil.render('index.html')

@app.route('/generic')
def generic():
    return templateutil.render('generic.html')

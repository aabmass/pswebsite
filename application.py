#!/usr/bin/env python3
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/generic')
def generic():
    return render_template('generic.html')

if __name__ == '__main__':
    app.debug = True
    app.run()

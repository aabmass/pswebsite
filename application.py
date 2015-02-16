#!/usr/bin/env python3
from flask import Flask
import views

app = Flask(__name__)

if __name__ == '__main__':
    app.debug = True
    app.run()

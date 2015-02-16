from flask.ext.login import UserMixin
from . import db

users = {}

class User(db.Model, UserMixin):
    # User Email information
    email = db.Column(db.String(255), nullable=False, unique=True, primary_key=True)

    # User Authentication information
    # Don't worry, it's hashed and salted first
    password = db.Column(db.String(255), nullable=False, default='')
    resetPasswordToken = db.Column(db.String(100), nullable=False, default='')


    # User information
    isEnabled = db.Column(db.Boolean(), nullable=False, default=True)
    firstName = db.Column(db.String(50), nullable=False, default='')
    lastName = db.Column(db.String(50), nullable=False, default='')

    def isActive(self):
        return self.isEnabled

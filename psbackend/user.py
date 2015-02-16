from flask.ext.login import UserMixin

users = {}

class User(UserMixin):
    def __init__(self, name):
        self.id = name
        self.name = name
        self.addToUsers()

    def get_id(self):
        return self.id

    def addToUsers(self):
        users[self.get_id()] = self

    def is_authenticated(self):
        return True
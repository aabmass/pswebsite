#!/usr/bin/env python3
import os
from psbackend import app
from psbackend import loginManager
from psbackend.user import User
from psbackend.user import users

@loginManager.user_loader
def load_user(userId):
    user = None
    if userId in users.keys():
        user = users[userId]
    return user

if ('PRODUCTION' in os.environ and
        os.environ['PRODUCTION'] == 'TRUE'):
    app.run(debug=False, host='0.0.0.0')
else:
    app.run(debug=True)

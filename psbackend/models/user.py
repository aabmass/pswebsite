from flask.ext.login import UserMixin
from werkzeug import security

from psbackend import db
from psbackend import loginManager

class User(db.Model, UserMixin):
    # User Email information
    email = db.Column(db.String(255), nullable=False, unique=True, primary_key=True)

    # User Authentication information
    passwordHash = db.Column(db.String(255), nullable=False, default='')
    resetPasswordToken = db.Column(db.String(100), nullable=False, default='')


    # User information
    isEnabled = db.Column(db.Boolean(), nullable=False, default=True)
    firstName = db.Column(db.String(50), nullable=False, default='')
    lastName = db.Column(db.String(50), nullable=False, default='')
    registeredOn = db.Column(db.Date(), nullable=False, default=db.DateTime)

    def __init__(self, email, password, firstName, lastName):
        self.email = email
        self.firstName = firstName
        self.lastName = lastName
        self.setPassword(password)

    ##
    # @brief Use this setter/getter; it salts properly!
    #
    # @param password the plain text password -- won't be saved
    def setPassword(self, password):
        self.passwordHash = security.generate_password_hash(password)

    def checkPassword(self, password):
        security.check_password_hash(self.passwordHash, password)

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

    def is_active(self):
        return True

    def get_id(self):
        return str(self.email)

    def save(self):
        db.session.add(self)
        db.session.commit()

@loginManager.user_loader
def loadUser(email):
    return User.query.get(email)

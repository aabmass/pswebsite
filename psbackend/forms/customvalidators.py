from wtforms import ValidationError
from psbackend.models import user

class LoginPasswordValidator():
    """ Validates that the given user exists in the database"""

    def __init__(self, message=None):
        self.message = "Username and/or password incorrect" or message

    def __call__(self, form, field):
        u = user.loadUser(form.email.data)

        if u is None:
            raise ValidationError("That username has not yet been registered.")
        elif not u.checkPassword(field.data):
            raise ValidationError("That password does not match the given username.")

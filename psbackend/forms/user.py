from wtforms import Form, BooleanField, StringField, PasswordField, validators

from psbackend.forms import customvalidators

from wtforms import Form, BooleanField, TextField, PasswordField, validators

class RegisterForm(Form):
    email = StringField('Email Address', [
        validators.Email("Not a valid Email Address"),
        validators.Required("Email Address is required")])
    firstName = StringField('First Name', [validators.Required()])
    lastName = StringField('Last Name', [validators.Required()])

    password = PasswordField('New Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password', [validators.Required()])

class LoginForm(Form):
    email = StringField('Email Address', [
        validators.Email(),
        validators.Required()])

    password = PasswordField('New Password', [
        customvalidators.LoginPasswordValidator(),
        validators.Required()])

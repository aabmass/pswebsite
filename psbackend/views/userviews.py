from flask import request, flash, redirect, url_for
from flask.ext.login import login_user, logout_user, login_required, current_user

from psbackend import app
from psbackend import templateutil
from psbackend.models.user import *
from psbackend.forms.user import RegisterForm, LoginForm

@app.route('/user')
@login_required
def user():
    return templateutil.render('user.html', pageTitle=current_user.get_id())

@app.route('/user/register', methods=['GET', 'POST'])
def register():
    registerForm = RegisterForm(request.form)

    print("\n{}\nvs:\n{}\n".format(request.form, registerForm.data))

    # Only validate the register form
    if request.method == "POST" and registerForm.validate():
        email = registerForm.email.data
        password = registerForm.password.data
        firstName = registerForm.firstName.data
        lastName = registerForm.lastName.data

        user = User(email=email, password=password,
                firstName=firstName, lastName=lastName)
        user.save()
        login_user(user)
        return redirect(request.args.get("next") or url_for("index"))

    return templateutil.render('logincreateuser.html', pageTitle="Login",
            loginForm=LoginForm(), registerForm=registerForm)

@app.route('/user/login', methods=['GET', 'POST'])
def login():
    """ Handles GET request for both logins and registrations """

    loginForm = LoginForm(request.form)

    # Only validate the login form
    if request.method == "POST" and loginForm.validate():
        user = loadUser(request.form["email"])

        # check to see if the given password hashes right
        login_user(user)
        return redirect(request.args.get("next") or url_for("index"))

    print("\n\n{}\n\n".format(loginForm.errors))

    return templateutil.render('logincreateuser.html', pageTitle="Login",
            loginForm=loginForm, registerForm=RegisterForm())


@app.route('/user/logout')
def logout():
    # logout the current user
    logout_user()
    flash("Logged out successfully")
    return redirect(request.args.get("next") or url_for("index"))

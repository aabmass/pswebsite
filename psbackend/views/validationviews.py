from flask import Response, request

from psbackend import app
from psbackend.models import user

@app.route('/user/validnewuser', methods=['GET', 'POST'])
def validnewuser():
    # email = request.form["email"]
    email = request.args["email"]

    print("Email {} is valid? {}".format(email, user.emailIsAvailable(email)))
    if user.emailIsAvailable(email):
        return Response(status=200)
    return Response(status=409)

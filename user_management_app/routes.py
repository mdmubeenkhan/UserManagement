from flask import Flask
from app import app

from user_management_app.models import User

@app.route('/login/user', methods=['GET'])
def user_login():
    return User.login()


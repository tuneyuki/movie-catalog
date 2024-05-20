# models.py
from flask_login import UserMixin
import os

class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    @staticmethod
    def get(user_id):
        if user_id == "1":
            username = os.getenv('USER_USERNAME')
            password = os.getenv('USER_PASSWORD')
            return User(user_id, username, password)
        return None

    @staticmethod
    def authenticate(username, password):
        stored_username = os.getenv('USER_USERNAME')
        stored_password = os.getenv('USER_PASSWORD')
        if username == stored_username and password == stored_password:
            return User("1", username, password)
        return None

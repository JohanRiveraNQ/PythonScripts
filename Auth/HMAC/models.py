from flask_login import UserMixin

# Simulación de una base de datos de usuarios
users = {
    "user1": {"password": "password1", "id": 1},
    "user2": {"password": "password2", "id": 2},
}

class User(UserMixin):
    def __init__(self, username):
        self.username = username
        self.id = users[username]["id"]

    def get_id(self):
        return self.id

    @staticmethod
    def authenticate(username, password):
        user = users.get(username)
        if user and user["password"] == password:
            return User(username)
        return None

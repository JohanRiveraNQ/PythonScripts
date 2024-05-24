class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.is_logged_in = False

    def login(self, entered_password):
        if entered_password == self.password:
            self.is_logged_in = True
            return True
        else:
            return False

    def logout(self):
        self.is_logged_in = False

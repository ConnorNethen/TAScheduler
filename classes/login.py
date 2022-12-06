from Scheduler.models import User


class Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        user = User.objects.filter(username=self.username, password=self.password)
        if user:
            return user[0]
        else:
            return None

    def logout(self):
        return None

    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password

    # Setters
    def setUsername(self, username):
        self.username = username

    def setPassword(self, password):
        self.password = password
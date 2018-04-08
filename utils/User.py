class User():
    def __init__(self, userId, userDisplay):
        self.userId = userId
        self.userDisplay = userDisplay
    def getId(self):
        return self.userId
    def getDisplay(self):
        return self.userDisplay

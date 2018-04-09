import re
from utils.Role import Role

class User():
    def __init__(self, userId, userDisplay):
        self.userId = userId
        self.userDisplay = userDisplay
        self.digits = re.compile("\d+")
        self.roles = []
    def getId(self):
        return self.userId
    def getDisplay(self):
        return self.userDisplay
    def addRole(self, display):
        self.roles.append(Role(display))
    def addRoles(self, l):
        for e in l:
            self.addRole(e)

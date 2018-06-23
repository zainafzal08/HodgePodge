from utils.User import User

class State():
    def __init__(self,author, members, location):
        self.author = author
        self.resolved = False
        self.members = set()
        for member in members:
            self.members.add(member)
        self.location = location

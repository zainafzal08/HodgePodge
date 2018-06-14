from utils.User import User

class State():
    def __init__(self,author_external, members, location):
        self.author = author_external
        self.resolved = False
        self.members = []
        for member in members:
            self.members.append(member)
        self.location = location

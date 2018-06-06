from utils.User import User

class State():
    def __init__(self,author_external_id, members, location):
        self.author = author_external_id
        self.resolved = False
        self.members = []
        for member_id in members:
            self.members.append(member_id)
        self.location = location

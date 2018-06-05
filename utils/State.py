from utils.User import User

class State():
    def __init__(self,author_external_id, members, location):
        self.author = User(author_external_id)
        self.members = []
        self.verified = False
        for member_id in members:
            self.members.append(User(member_id))
        self.location = location

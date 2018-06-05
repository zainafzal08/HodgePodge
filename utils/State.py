class State():
    def __init__(self,external_id, members, location):
        self.user = User(external_id)
        self.members = []
        self.verified = False
        for member_id in members:
            self.members.append(User(member_id))
        self.location = location

from utils.Response import Response
from utils.Parser import Parser
from utils.Response import Response
from utils.Database import Db
from utils.Daddy import Daddy

import inspect

class HodgePodge():
    def __init__(self, dbConnString):
        self.modules = []
        self.db = Db(dbConnString)
        self.daddy = Daddy(self.db)
        self.parser = Parser(self.daddy)

    def attachModule(self, m):
        self.modules.append(m)
        m.connectParser(self.parser)
        m.connectDb(self.db)
        m.__daddy__ = self.daddy
        self.flushModule(m)

    # ok now i admit. this is a hacky way to do this **BUT**
    # unless someone else makes a function called wrapped_f
    # i should be safe....
    def flushModule(self, m):
        for member in inspect.getmembers(m):
            if inspect.ismethod(member[1]):
                if member[1].__name__ == "wrapped_f":
                    member[1].__call__()

    def processRequest(response, request):
        pass

    def doYouKnow(self, id):
        return self.daddy.knows(id)

    # Registers a new user with hodge podge
    def newUser(self, id, display, **kargs):
        if self.daddy.knows(id):
            raise Exception("User already exists in database")
        self.daddy.meet(id,display,kargs)

    # registers a new role with hodge podge
    def newRole(self, id, display, **kargs):
        if self.daddy.knowsRole(id):
            raise Exception("Role already exists in database")
        self.daddy.newRole(id,display,kargs)

    # gives user role
    def giveRole(self, userId, roleId):
        if not self.daddy.knowsRole(roleId):
            raise Exception("Unknown Role")
        if not self.daddy.knows(userId):
            raise Exception("Unknown User")
        self.daddy.pwease(userId,roleId)

    def talk(self, message, user, locationId, members):
        user = self.daddy.getUser(user)
        members = self.daddy.getUsers(members)
        # manage users/members
        if len(members) == 0 and user == None:
            return None
        match = self.parser.parse(message,user,locationId, members)
        if not match:
            return None
        r = match.trigger()
        return r

from utils.Response import Response
from utils.Parser import Parser
from utils.Response import Response
from utils.Database import Db

import inspect

class HodgePodge():
    def __init__(self, dbConnString):
        self.modules = []
        self.parser = Parser()
        self.db = Db(dbConnString)

    def attachModule(self, m):
        self.modules.append(m)
        m.connectParser(self.parser)
        m.connectDb(self.db)
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

    def talk(self, message, user, locationId, members):
        # If there is a member we don't know of, make a entry for them
        raise Exception("Add new users to users database")
        # Get user objects for all members present
        raise Exception("Retrive users by their secret keys etc.")

        match = self.parser.parse(message,user,locationId, members)
        if not match:
            return None
        r = match.trigger()
        return r

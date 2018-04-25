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

    def talk(self, message, user, locationId, members):
        members = self.daddy.verify(members)
        if len(members) == 0:
            return None
        match = self.parser.parse(message,user,locationId, members)
        if not match:
            return None
        r = match.trigger()
        return r

from utils.Response import Response
from utils.Parser import Parser
from utils.Response import Response
import inspect

class HodgePodge():
    def __init__(self, dbURL):
        self.modules = []
        self.parser = Parser()
        self.dbURL = "db/test.db"

    def kill(self):
        pass

    def attach_module(self, m):
        self.modules.append(m)
        m.connect_parser(self.parser)
        self.flush_modules(m)

    # ok now i admit. this is a hacky way to do this **BUT**
    # unless someone else makes a function called wrapped_f
    # i should be safe....
    def flush_modules(self, m):
        for member in inspect.getmembers(m):
            if inspect.ismethod(member[1]):
                if member[1].__name__ == "wrapped_f":
                    member[1].__call__()

    def resolve_state(self, state):
        state.author.resolve(self.dbURL)
        for member in state.members:
            member.resolve(self.dbURL)

    def talk(self, state, msg):
        self.resolve_state(state)
        m = self.parser.parse(state,msg)
        if m:
            return m.trigger()
        return None

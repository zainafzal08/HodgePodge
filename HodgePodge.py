from utils.Response import Response
from utils.Parser import Parser
from utils.Response import Response
from utils.Daddy import Daddy
import inspect

class HodgePodge():
    def __init__(self):
        self.modules = []
        self.daddy = Daddy()
        self.parser = Parser(self.daddy)

    def kill(self):
        pass

    def attach_module(self, m):
        self.modules.append(m)
        m.connect_parser(self.parser)
        m.__daddy__ = self.daddy
        self.flush_modules(m)

    # ok now i admit. this is a hacky way to do this **BUT**
    # unless someone else makes a function called wrapped_f
    # i should be safe....
    def flush_modules(self, m):
        for member in inspect.getmembers(m):
            if inspect.ismethod(member[1]):
                if member[1].__name__ == "wrapped_f":
                    member[1].__call__()

    def talk(self, state, msg):
        state = self.daddy.resolve_state(state)
        m = self.parser.parse(state,msg)
        return m.trigger()

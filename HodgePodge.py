from utils.Response import Response
from utils.Parser import Parser
from utils.Response import Response
from exceptions.Interface import InterfaceException
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import inspect
# Import all classes
from utils.Base import Base
from utils.User import User

class HodgePodge():
    def __init__(self, dbURL):
        self.modules = []
        self.parser = Parser()
        #DB stuff
        self.db_engine = create_engine(dbURL)
        Base.metadata.create_all(self.db_engine)
        Base.metadata.bind = self.db_engine
        DBSession = sessionmaker()
        DBSession.bind = self.db_engine
        self.db_session = DBSession()

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

    def get_user(self, id):
        q = self.db_session.query(User).filter(User.external_id == id).all()
        if not len(q):
            u = User(external_id=id, display_name=None)
            self.db_session.add(u)
            self.db_session.commit()
            return u
        return q[0]

    def resolve_state(self, state):
        if state.resolved:
            self.db_session.refresh(state.author)
            [self.db_session.refresh(m) for m in state.members]
        else:
            state.resolved = True
            state.author = self.get_user(state.author)
            state.members = [self.get_user(m) for m in state.members]

    def talk(self, state, msg):
        self.resolve_state(state)
        m = self.parser.parse(state,msg)
        self.db_session.commit()
        if m:
            return m.trigger()
        return None

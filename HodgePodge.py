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
from utils.Permissions import Permissions

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
        m.__connect_parser__(self.parser)
        m.__boy__ = self
        m.permissions = self.get_permissions(m.name)
        self.flush_modules(m)
        # let the module know it's been mounted
        m.mounted()

    def is_module(self, module):
        return module.lower() in [m.name.lower() for m in self.modules]

    def get_func_doc(self, obj, func_name):
        d = obj.__fdocs__.get(func_name,None)
        if not d:
            return ""
        d = d.strip()
        example = d.split("\n")[0].strip()
        desc = d.split("\n")[1].strip()
        return (example,desc)

    def get_module_doc(self, obj_name, user, location):
        obj = self.get_module_obj(obj_name)
        raw = obj.__doc__.strip()
        tmp = []
        for l in raw.split("\n"):
            tmp.append(l.strip())
        raw = "\n".join(tmp)
        func_list = self.parser.get_function_list(obj.name, user, location)
        func_docs = ["  > %s - %s\n      %s"%(f,self.get_func_doc(obj, f)[0],self.get_func_doc(obj, f)[1]) for f in func_list]
        func_docs = "\n".join(func_docs)
        return "```\n%s\n%s\n```"%(raw,func_docs)

    def get_module_obj(self, module):
        if not self.is_module(module):
            raise InterfaceException("Invalid Module Supplied")
        return [m for m in self.modules if m.name.lower() == module][0]

    # ok now i admit. this is a hacky way to do this **BUT**
    # unless someone else makes a function called wrapped_f
    # i should be safe....
    def flush_modules(self, m):
        for member in inspect.getmembers(m):
            if inspect.ismethod(member[1]):
                if member[1].__name__ == "wrapped_f":
                    member[1].__call__()

    def get_permissions(self, module_name):
        return Permissions(module_name)

    def get_user(self, usr):
        id = usr[0]
        tags = usr[1]
        q = self.db_session.query(User).filter(User.external_id == id).all()
        u  = None
        if not len(q):
            qu = User(external_id=id, display_name=None)
            self.db_session.add(u)
            self.db_session.commit()
            u = qu
        else:
            u = q[0]
        u.set_tags(tags)
        return u

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

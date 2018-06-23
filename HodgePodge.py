from utils.Response import Response
from utils.Parser import Parser
from utils.Response import Response
from exceptions.Interface import InterfaceException
import psycopg2
import sqlite3
import urllib.parse as urlparse
import inspect
import re
# Import all classes
from utils.User import User
from utils.Permissions import Permissions

class HodgePodge():
    def __init__(self, dbURL):
        self.modules = []
        self.parser = Parser()
        #DB stuff
        self.db_url = dbURL
        self.db_conn = None
        self.open_db()

    def open_db(self):
        url = urlparse.urlparse(self.db_url)
        dbname = url.path[1:]
        user = url.username
        password = url.password
        host = url.hostname
        port = url.port
        self.db_conn = psycopg2.connect(dbname=dbname,user=user,password=password,host=host,port=port)

    def close_db(self):
        self.db_conn.close()
        self.db_conn = None

    def kill(self):
        self.close_db()

    def __del__(self):
        self.kill()

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

    def get_module_list(self):
        return "```\n%s\n```"%"\n".join([x.name for x in self.modules])
    def get_func_doc(self, obj, func_name):
        d = obj.__fdocs__.get(func_name,None)
        if not d:
            return ""
        d = d.strip()
        example = d.split("\n")[0].strip()
        desc = "\n".join(["       "+l.strip() for l in d.split("\n")[1:]])
        return (example,desc)

    def get_module_doc(self, obj_name, user, location):
        obj = self.get_module_obj(obj_name)
        raw = obj.__doc__.strip()
        tmp = []
        for l in raw.split("\n"):
            tmp.append(l.strip())
        raw = "\n".join(tmp)
        func_list = self.parser.get_function_list(obj.name, user, location)
        func_docs = ["  > %s - %s\n%s"%(f,self.get_func_doc(obj, f)[0],self.get_func_doc(obj, f)[1]) for f in func_list]
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

    # lazy resolve
    def resolve_state(self, state):
        state.author.set_db(self.db_conn)
        for m in state.members:
            m.set_db(self.db_conn)

    def talk(self, state, msg):
        # open up
        self.resolve_state(state)
        # respond
        m = self.parser.parse(state,msg)
        r = None
        if m:
            r = m.trigger()
        return r

class Module():
    def __init__(self,name):
        self.name = name
    def connectParser(self, p):
        self.__parser__ = p
    def getParser(self):
        return self.__parser__
    def validate(self, raw, id):
        return None
    def connectDb(self, db):
        self.__db__ = db
    def getDb(self):
        return self.__db__


class Trigger():
    def __init__(self,regex,access,grpIds):
        self.regex = regex
        self.access = access
        self.initalised = False
        self.grpIds = grpIds

    def createPermissions(self, m):
        r = {
            "TABLE": "PERMISSIONS",
            "FIELDS": {
                "MODULE": "TEXT",
                "FUNCTION": "TEXT",
                "PERMISSIONS": "TEXT"
            },
            "EXISTS": None
        }
        m.getDb().register(r)

    def registerPermissions(self, m, fn, access):
        access = ",".join(list(map(lambda x: x.getId())))
        r = {
            "TABLE": "PERMISSIONS",
            "SET": ["MODULE","FUNCTION","PERMISSIONS"],
            "WHERE": {
                "MODULE": m.name,
                "FUNCTION": fn
            },
            "VALUE": [m.name,fn,access],
            "FORCE": True
        }
        m.getDb().edit(r)

    def __call__(self,f,**args):
        def wrapped_f(*args):
            if not self.initalised:
                args[0].getParser().register(args[0],self.regex,f.__name__,self.grpIds)
                self.createPermissions(args[0])
                self.registerPermissions(args[0],f.__name__,self.access)
                self.initalised = True
            else:
                return f(*args)
        return wrapped_f

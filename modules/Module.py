from utils.Permissions import Rule, Behaviour

class Module():
    def __init__(self,name):
        self.name = name
        self.permissions = None
        self.__boy__ = None
    def __connect_parser__(self, p):
        self.__parser__ = p
    def __get_parser__(self):
        return self.__parser__
    def validate(self, raw, id):
        return None
    def mounted(self):
        pass

class Trigger():
    def __init__(self,regex,grpIds):
        self.regex = regex
        self.initalised = False
        self.grpIds = grpIds
    def __call__(self,f,**args):
        def wrapped_f(*args):
            if not self.initalised:
                m = args[0]
                m.__get_parser__().register(args[0],self.regex,f.__name__,self.grpIds)
                m.permissions.set_rule(f.__name__,Rule(Behaviour.ALL))
                self.initalised = True
            else:
                return f(*args)
        return wrapped_f

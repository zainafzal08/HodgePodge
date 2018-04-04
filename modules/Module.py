class Module():
    def __init__(self):
        pass
    def connectParser(self, p):
        self.parser = p
    def getParser(self):
        return self.parser
    def validate(self, raw, id):
        return None

class Trigger():
    def __init__(self,regex,access,grpIds):
        self.regex = regex
        self.access = access
        self.initalised = False
        self.grpIds = grpIds
    def __call__(self,f,**args):
        def wrapped_f(*args):
            if not self.initalised:
                args[0].getParser().register(args[0],self.regex,self.access,f.__name__,self.grpIds)
                self.initalised = True
            else:
                return f(*args)
        return wrapped_f

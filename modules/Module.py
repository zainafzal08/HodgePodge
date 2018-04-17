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
    def __init__(self,regex,grpIds):
        self.regex = regex
        self.initalised = False
        self.grpIds = grpIds

    def __call__(self,f,**args):
        def wrapped_f(*args):
            if not self.initalised:
                args[0].getParser().register(args[0],self.regex,f.__name__,self.grpIds)
                self.initalised = True
            else:
                return f(*args)
        return wrapped_f

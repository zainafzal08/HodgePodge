class Module():
<<<<<<< HEAD
    def __init__(self, name):
        self.name = name


    def blankRes(self):
        res = {}
        res["output"] = []
        res["channel_output_target"] = ""
        res["channel_output"] = ""
        return res

    def trigger(self, message, requestLevel):
        return self.blankRes()
=======
    def __init__(self,name):
        self.name = name
        # god help me i hope this doesn't result in a exploit
        self.__daddy__ = None
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
                m = args[0]
                m.getParser().register(args[0],self.regex,f.__name__,self.grpIds)
                m.__daddy__.registerTrigger(m,f)
                self.initalised = True
            else:
                return f(*args)
        return wrapped_f
>>>>>>> 9dc43570a5b796e49e1942c78d9499f802eb8a02

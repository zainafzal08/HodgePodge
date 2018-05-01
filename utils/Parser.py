import re
from utils.Response import Response

class Context():
    def __init__(self):
        self.groups = []
        self.locationId = None
        self.raw = None
        self.user = None
        self.members = []
        self.idMap = {}
    def getNumber(self, i):
        e = self.groups[i]
        if e:
            return int(re.sub('\s+','',e))
        return None
    def getString(self, i):
        return self.groups[i]
    def getMembers(self):
        return self.members
    def getUser(self):
        return self.users
    def getGroup(self, n):
        if n in self.idMap:
            return self.groups[self.idMap[n]]
        return None
class Match():
    def __init__(self, m, rgx, f,grpIds):
        self.module = m
        self.regex = re.compile(rgx)
        self.function = f
        self.groupId = grpIds
        self.context = Context()

    def trigger(self):
        valid = True
        err = None
        for i,g in enumerate(self.context.groups):
            if i >= len(self.groupId):
                break
            v = self.module.validate(g,self.groupId[i])
            if v:
                err = v
                break
        if not err:
            return getattr(self.module,self.function)(self.context)
        else:
            res = Response()
            res.textResponce("_bzzt_ %s"%err,self.context.locationId,"err")
            return res

class Parser():
    def __init__(self, daddy):
        self.triggers = []
        self.daddy = daddy
        pass

    def register(self, m, rgx, f, grpIds):
        match = Match(m,rgx, f, grpIds)
        self.triggers.append(match)

    def permission(self, user, trigger):
        # ask Daddy if user has permission
        if daddy.pweaseTwigger(trigger.m, trigger.function, user):
            return True
        return False

    def parse(self, message, author, locationId ,members):
        m = message.lower()
        for trigger in self.triggers:
            s = trigger.regex.search(m)
            if s and self.permission(author, trigger):
                trigger.context.groups = s.groups()
                trigger.context.raw = message
                trigger.context.locationId = locationId
                trigger.context.user = author
                trigger.context.members = members
                for e,i in enumerate(trigger.groupId):
                    trigger.context.idMap[e] = i
                return trigger
            else:
                continue
        return None

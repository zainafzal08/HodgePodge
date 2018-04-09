import re
from utils.Response import Response

class Context():
    def __init__(self):
        self.groups = []
        self.locationId = None
        self.raw = None
        self.user = None
        self.members = []
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
    def __init__(self):
        self.triggers = []
        pass

    def register(self, m, rgx, f, grpIds):
        match = Match(m,rgx, f, grpIds)
        self.triggers.append(match)

    def permission(self, user, trigger):
        raise Exception("QUERY THE DB DIPSHIT")
        if len(access) == 0:
            return True
        for r in roles:
            if r in access:
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
                return trigger
            else:
                continue
        return None

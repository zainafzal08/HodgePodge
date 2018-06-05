import re
from utils.Response import Response

class Context():
    def __init__(self):
        self.groups = []
        self.location_id = None
        self.raw = None
        self.user = None
        self.members = []
        self.id_map = {}
    def get_number(self, i):
        e = self.groups[i]
        if e:
            return int(re.sub('\s+','',e))
        return None
    def get_string(self, i):
        return self.groups[i]
    def get_members(self):
        return self.members
    def get_author(self):
        return self.author
    def get_group(self, n):
        if n in self.id_map:
            return self.groups[self.id_map[n]]
        return None

class Match():
    def __init__(self, m, rgx, f,grpIds):
        self.module = m
        self.regex = re.compile(rgx)
        self.function = f
        self.group_id = grpIds
        self.context = Context()

    def trigger(self):
        valid = True
        err = None
        for i,g in enumerate(self.context.groups):
            if i >= len(self.group_id):
                break
            v = self.module.validate(g,self.group_id[i])
            if v:
                err = v
                break
        if not err:
            return getattr(self.module,self.function)(self.context)
        else:
            res = Response()
            res.textResponce("_bzzt_ %s"%err,self.context.location_id,"err")
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
        if self.daddy.can_trigger(trigger.module, trigger.function, user):
            return True
        return False

    def parse(self, state, message):
        author = state.author
        location_id = state.location
        members = state.members
        m = message.lower()
        for trigger in self.triggers:
            s = trigger.regex.search(m)
            if s and self.permission(author, trigger):
                trigger.context.groups = s.groups()
                trigger.context.raw = message
                trigger.context.location_id = location_id
                trigger.context.author = author
                trigger.context.members = members
                for e,i in enumerate(trigger.group_id):
                    trigger.context.id_map[e] = i
                return trigger
            else:
                continue
        return None

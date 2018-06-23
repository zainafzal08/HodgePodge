from enum import Enum
from exceptions.Interface import InterfaceException

class Behaviour(Enum):
    ALL = 1
    NONE = 2
    BLOCK_FIRST = 3
    ALLOW_FIRST = 4

class Rule:
    # assume users know what they are doing
    # enforcing typing is annoying in python :(
    def __init__(self, default, **kargs):
        self.default = default
        self.allowed_tags = kargs.get("allowed_tags",set())
        self.blocked_tags = kargs.get("blocked_tags",set())
        self.blacklist = kargs.get("blacklist",set())
        self.whitelist = kargs.get("whitelist",set())
        self.admin_only = kargs.get("admin_only",False)
        self.tie_behavior = kargs.get("tie_behavior",Behaviour.BLOCK_FIRST)
        self.location_blacklist = kargs.get("location_blacklist",set())
        self.location_whitelist = kargs.get("location_whitelist",set())

    def boolean_check(self,black,white):
        if black and white:
            if self.tie_behavior == Behaviour.ALLOW_FIRST:
                return True
            else:
                return False
        elif black:
            return False
        elif white:
            return True
        return None

    def test(self, location, user):
        # test admin status first
        if user.admin:
            return True
        elif self.admin_only:
            return False
        # test location permission
        in_black_loc = location in self.location_blacklist
        in_white_loc = location in self.location_whitelist
        r = self.boolean_check(in_black_loc,in_white_loc)
        if r != None:
            return r
        # test if on blacklist or whitelist first
        in_black = user in self.blacklist
        in_white = user in self.whitelist
        r = self.boolean_check(in_black,in_white)
        if r != None:
            return r
        # check if allowed in tags
        in_allowed = True if len(user.get_tags() & self.allowed_tags) > 0 else False
        in_blocked = True if len(user.get_tags() & self.blocked_tags) > 0 else False
        r = self.boolean_check(in_blocked,in_allowed)
        if r != None:
            return r
        # return default if user has no assoicated rules
        return True if self.default == Behaviour.ALL else False

class Permissions:
    def __init__(self,name):
        self.ref_name = name
        self.rules = {}

    def set_rule(self, function, rule):
        # make a merge once db is ready
        # (only overide things user has specified)
        self.rules[function] = rule

    def get_rule(self, function):
        return self.rules.get(function,None)

    def test(self, function, location, user):
        if function not in self.rules:
            raise InterfaceException("Unknown Function Specified")
        return self.rules[function].test(location, user)

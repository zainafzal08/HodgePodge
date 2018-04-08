from modules.Module import Module, Trigger
from utils.Response import Response
from utils.misc import *
import os
import re

class Utility(Module):
    def __init__(self):
        super().__init__("Utility")

    def validate(self, raw, id):
        if not raw:
            return None
        if id == "m":
            try:
                eval(re.sub('\s+','',raw))
                return None
            except:
                return "Much like my opinion of you, that expression is malformed"
        return None

    @Trigger('hodge podge.*pick someone',[],[])
    def pick(self, context):
        members = context.getMembers()
        target = pick(members)
        res = Response()
        resText = "I Have Chosen %s."%(target.getDisplay())
        res.textResponce(resText,context.locationId,"output")
        return res

    @Trigger('hodge podge calc(ulate)? ([\+\-\d\*\/e\^\(\)\s]*)',[],[None,"m"])
    def calc(self, context):
        expr = re.sub('\s+','',context.groups[1])
        expr = eval(expr)
        res = Response()
        resText = "By my calculations thats %s"%(str(expr))
        res.textResponce(resText,context.locationId,"output")
        return res

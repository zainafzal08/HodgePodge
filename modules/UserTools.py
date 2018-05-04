from modules.Module import Module, Trigger
from utils.Response import Response
from utils.misc import *
import os
import re

class UserTools(Module):
    def __init__(self):
        super().__init__("UserTools")

    def validate(self, raw, id):
        return None

    @Trigger('hodge podge call me (.*)$',[])
    def nameUpdate(self, context):
        user = context.getUser()
        name = context.getString(0)
        self.__daddy__.updateDisplay(user,name)
        res = Response()
        resText = "I'll remember that %s ;)"%(name)
        res.textResponce(resText,context.locationId,"output")
        return res

    @Trigger('hodge podge what\'?s? my id',[])
    def getId(self, context):
        user = context.getUser()
        res = Response()
        resText = "It's %s"%(self.__daddy__.generateLinkingId(user))
        res.textResponce(resText,context.locationId,"output")
        return res

    @Trigger('hodge podge my id is (\w+)',[None])
    def setId(self, context):
        user = context.getUser()
        hid = context.getString(0)
        self.__daddy__.link(user,hid)
        res = Response()
        resText = "Oh of course! I'll remember that"
        res.textResponce(resText,context.locationId,"output")
        return res

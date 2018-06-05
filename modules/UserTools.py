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

    @Trigger('hodge podge what\'?s? my name',[])
    def nameUpdate(self, context):
        user = context.getUser()
        name = context.getString(0)
        display = self.__daddy__.getDisplay(user)
        res = Response()
        resText = "You are %s!"%display
        res.textResponce(resText,context.locationId,"output")
        return res

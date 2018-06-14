from modules.Module import Module, Trigger
from utils.Response import Response
from utils.misc import *
from utils.Permissions import Permissions, Behaviour, Rule
import os
import re

class Utility(Module):
    '''
    Utility Module
    =======================================================
    A simple module to provide some useful tools
    -------------------------------------------------------
    '''
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
        elif id == "module":
            if self.__boy__.is_module(raw):
                return None
            else:
                return "Given that the module doesn't exist, you don't."
        return None

    @Trigger('hodge podge.*pick someone',[])
    def pick(self, context):
        '''
        Hodge podge pick someone
        Picks a random person from the current chat
        '''
        members = context.get_members()
        target = pick(members)
        res = Response()
        resText = "I Have Chosen %s."%(target.get_display())
        res.text_responce(resText,context.location_id,"output")
        return res

    @Trigger('hodge podge calc(ulate)? ([\+\-\d\*\/e\^\(\)\s]*)',[None,"m"])
    def calc(self, context):
        '''
        Hodge podge calculate 1+1
        Evaluates a mathematical expression
        '''
        expr = re.sub('\s+','',context.groups[1])
        expr = eval(expr)
        res = Response()
        resText = "By my calculations thats %s"%(str(expr))
        res.text_responce(resText,context.location_id,"output")
        return res

    @Trigger('hodge podge how do i use( the)? (\w+)( module)?',[None,"module"])
    def help(self, context):
        '''
        Hodge podge how do i use the utility module
        Displays help docs
        '''
        module = context.get_string(1)
        res = Response()
        resText = self.__boy__.get_module_doc(module, context.author, context.location_id)
        res.text_responce(resText,context.location_id,"output")
        return res

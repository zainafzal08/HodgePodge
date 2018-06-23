from modules.Module import Module, Trigger
from utils.Response import Response
from utils.misc import *
from utils.Permissions import Permissions, Behaviour, Rule
import os
import re

class UserTools(Module):
    '''
    User Tools
    =======================================================
    A simple module to provide a interface to your
    hodge podge user state
    -------------------------------------------------------
    '''
    def __init__(self):
        super().__init__("UserTools")

    def mounted(self):
        r = Rule(Behaviour.ALL, admin_only=True)
        self.permissions.set_rule("list_users",r)

    def validate(self, raw, id):
        return None

    @Trigger('hodge podge call me (.*)$',[])
    def name_update(self, context):
        '''
        Hodge podge call me beautiful
        sets the nickname hodge podge will call you by
        '''
        user = context.get_author()
        name = context.get_string(0)
        user.display_name = name
        res = Response()
        resText = "I'll remember that %s ;)"%(name)
        res.text_responce(resText,context.location_id,"output")
        return res

    @Trigger('hodge podge what\'?s? my name',[])
    def name_get(self, context):
        '''
        Hodge podge what's my name
        Tells you the current nickname hodge podge has for you
        '''
        user = context.get_author()
        display = user.display_name
        res = Response()
        if display:
            resText = "You are %s!"%display
        else:
            resText = "I don't know your name! Feel free to introduce yourself, just say something along the lines of `Hodge Podge call me xX_minecraft_p0rn_Xx`"
        res.text_responce(resText,context.location_id,"output")
        return res

    @Trigger('hodge podge list( all)? users',[])
    def list_users(self, context):
        '''
        Hodge podge list users [ADMIN_ONLY]
        Lists user details for all users in current location
        '''
        author = context.get_author()
        res = Response()
        resText = []
        for user in context.members+[author]:
            tgs = list(sorted([e for e in user.get_tags()]))
            resText.append("%s : %s"%(user.get_display(),tgs))
        resText = "\n".join(resText)
        resText = "```%s```"%resText
        res.text_responce(resText,context.location_id,"output")
        return res

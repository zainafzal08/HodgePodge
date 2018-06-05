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
    def name_update(self, context):
        user = context.get_author()
        name = context.get_string(0)
        self.__daddy__.update_display(user,name)
        res = Response()
        resText = "I'll remember that %s ;)"%(name)
        res.text_responce(resText,context.location_id,"output")
        return res

    @Trigger('hodge podge what\'?s? my name',[])
    def name_get(self, context):
        user = context.get_author()
        display = user.display_name
        res = Response()
        if display:
            resText = "You are %s!"%display
        else:
            resText = "I don't know your name! Feel free to introduce yourself, just say something along the lines of `Hodge Podge call me xX_minecraft_p0rn_Xx`"
        res.text_responce(resText,context.location_id,"output")
        return res

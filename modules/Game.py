from modules.Module import Module, Trigger
from utils.Response import Response
from utils.misc import *
import os
import re

# enforce the parser stuff
class Game(Module):

    def __init__(self):
        super().__init__("Game")
        self.dice_type_range = (1,1000)
        self.dice_num_range = (1,1000)

    def validate(self, raw, id):
        if raw == None:
            return None
        if id == "d":
            d = int(re.sub('\s+','',raw))
            if d >= self.dice_type_range[0] and d <= self.dice_type_range[1]:
                return None
            return "I can only handle d%d to d%d"%self.dice_type_range
        elif id == "dn":
            d = int(re.sub('\s+','',raw))
            if d >= self.dice_num_range[0] and d <= self.dice_num_range[1]:
                return None
            return "I can only handle %d to %d rolls"%self.dice_num_range
        elif id == "m":
            m = int(re.sub('\s+','',raw))
            if m >= -1000000000000 and m <= 1000000000000:
                return None
            return "What kind of mod is that?!"
        return None

    @Trigger('hodge podge.*roll.*d\s*(\-?\d+)\s*([\+\-]\s*\d+)?',["d","m"])
    def roll(self, context):
        dice_type = context.get_number(0)
        mod = context.get_number(1)
        modPf = None
        if mod:
            modPf = "+" if mod > 0 else ""
        res = Response()
        r = random_num(1,dice_type)
        resText = "I Got %d [%d%s%d]!"%(r+mod,r,modPf,mod) if mod else "I Got %d!"%(r)
        res.text_responce(resText,context.location_id,"output")
        return res

    @Trigger('hodge podge.*roll[^\d]*(\d+)[^d]*d\s*(\-?\d+)s?\s*([\+\-]\s*\d+)?',["dn","d","m"])
    def multiroll(self, context):
        # set up
        res = Response()
        dice_num = context.get_number(0)
        dice_type = context.get_number(1)
        mod = context.get_number(2)
        modPf = None
        if mod:
            modPf = "+" if mod > 0 else ""
        # calculate
        components = []
        sum = 0
        for i in range(dice_num):
            d = random_num(1,dice_type)
            sum += d
            components.append(str(d))
        roll_rtr = "I got %d!"%(sum+mod) if mod else "I got %d!"%sum
        component_str = " (%s[%s%d])"%("+".join(components),modPf,mod) if mod else " (%s)"%("+".join(components))
        #TODO: shift this into text responce
        if len(roll_str) + len(component_str) < 2000:
            roll_str += component_str
        res.text_responce(roll_str,context.location_id,"out")
        return res

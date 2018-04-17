from modules.Module import Module, Trigger
from utils.Response import Response
from utils.Formatter import Formatter
from utils.misc import *
import os
import re

# enforce the parser stuff
class Game(Module):
    def __init__(self):
        self.formatter = Formatter()
        self.diceTypeRange = (1,1000)
        self.diceNumRange = (1,1000)
        super().__init__("Game")

    def validate(self, raw, id):
        if not raw:
            return None
        if id == "d":
            d = int(re.sub('\s+','',raw))
            if d >= self.diceTypeRange[0] and d <= self.diceTypeRange[1]:
                return None
            return "I can only handle d%d to d%d"%self.diceTypeRange
        elif id == "dn":
            d = int(re.sub('\s+','',raw))
            if d >= self.diceNumRange[0] and d <= self.diceNumRange[1]:
                return None
            return "I can only handle %d to %d rolls"%self.diceNumRange
        elif id == "m":
            m = int(re.sub('\s+','',raw))
            if m >= -1000000000000 and m <= 1000000000000:
                return None
            return "What kind of mod is that?!"
        return None

    @Trigger('hodge podge.*roll.*d\s*(\-?\d+)\s*([\+\-]\s*\d+)?',["d","m"])
    def roll(self, context):
        diceType = context.getNumber(0)
        mod = context.getNumber(1)
        modPf = None
        if mod:
            modPf = "+" if mod > 0 else ""
        res = Response()
        r = randomNum(1,diceType)
        resText = "I Got %d [%d%s%d]!"%(r+mod,r,modPf,mod) if mod else "I Got %d!"%(r)
        res.textResponce(resText,context.locationId,"output")
        return res

    @Trigger('hodge podge.*roll[^\d]*(\d+)[^d]*d\s*(\-?\d+)s?\s*([\+\-]\s*\d+)?',["dn","d","m"])
    def multiroll(self, context):
        # set up
        res = Response()
        diceNum = context.getNumber(0)
        diceType = context.getNumber(1)
        mod = context.getNumber(2)
        modPf = None
        if mod:
            modPf = "+" if mod > 0 else ""
        # calculate
        components = []
        sum = 0
        for i in range(diceNum):
            d = randomNum(1,diceType)
            sum += d
            components.append(str(d))
        rollStr = "I got %d!"%(sum+mod) if mod else "I got %d!"%sum
        componentStr = " (%s[%s%d])"%("+".join(components),modPf,mod) if mod else " (%s)"%("+".join(components))
        if len(rollStr) + len(componentStr) < 2000:
            rollStr += componentStr
        res.textResponce(rollStr,context.locationId,"out")
        return res

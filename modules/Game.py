<<<<<<< HEAD
from modules.Module import Module
import re
import random
from random import randint
from discord.utils import find

class Game(Module):
    def __init__(self, db):
        super().__init__("Game")
        self.commands = [
            ("hodge podge roll a d\d+\s*$", self.roll),
            ("hodge podge roll \d+ d\d+s?\s*$", self.multiRoll),
            ("hodge podge give .* \d+ .* points?\s*$", self.editPoints),
            ("hodge podge take \d+ .* points? from .*\s*$", self.editPoints),
            ("hodge podge list all score types\s*$", self.listPoints),
            ("hodge podge summerise .* points?\s*$", self.getPoints),
            ("hodge podge give me a name\s*$", self.getName)
        ]
        self.db = db
        self.scoreEditLevel = 0

    def multiRoll(self, message, level):
        s = re.search(r"hodge podge roll (\d+) d(\d+)s?\s*$",self.clean(message.content))
        count = int(s.group(1))
        d = int(s.group(2))
        res = super().blankRes()
        if d > 1000 or count > 1000:
            res["output"].append("Sorry friend! That number is too big")
        else:
            roll = 0
            components = []
            for i in range(count):
                r = random.randint(1,d)
                roll += r
                components.append(str(r))
            roll = str(roll)
            componentString = "+".join(components)
            if len(components) > 100:
                res["output"].append("I got "+roll+"!")
            else:
                res["output"].append("I got "+roll+"! ("+componentString+")")
        return res

    def roll(self, message, level):
        s = re.search(r"hodge podge roll a d(\d+)\s*$",self.clean(message.content))
        d = int(s.group(1))
        res = super().blankRes()
        if d > 1000:
            res["output"].append("Sorry friend! That number is too big")
        else:
            roll = str(random.randint(1,d))
            res["output"].append("It landed on "+roll+"!")
        return res

    def editPoints(self, message, level):
        if level < self.scoreEditLevel:
            return

        s1 = re.search(r"hodge podge give (.*) (\d+) (.*) points?\s*$",self.clean(message.content))
        s2 = re.search(r"hodge podge take (\d+) (.*) points? from (.*)\s*$",self.clean(message.content))

        if s1:
            s = s1
            score = int(s.group(2))
            scoreType = self.shallowClean(s.group(3))
        elif s2:
            s = s2
            score = int(s.group(1))*-1
            scoreType = self.shallowClean(s.group(2))

        person = None
        if len(message.mentions) != 0:
            person = message.mentions[0]
        res = super().blankRes()

        if not person:
            res["output"].append("Sorry! I don't know who to target! Did you make sure to use a valid `@` mention?")
        else:
            new = self.db.scoreEdit(message.channel.id, scoreType, person.id, score)
            res["output"].append(person.name + " now has "+str(new)+" points!")
        return res

    def getName(self, message, level):
        if level < 0:
            return
        vowels = ["a","e","i","o","u"]
        f = open("words.txt","r")
        raw = f.read()
        f.close()
        l = raw.split("\n")
        w = l[randint(0,len(l)-1)]
        a = randint(0,len(w)-1)
        b = a
        while a == b:
        	b = randint(0,len(w))
        v1 = vowels[randint(0,len(vowels)-1)]
        v2 = vowels[randint(0,len(vowels)-1)]
        w = list(w)
        w.insert(a,v1)
        w.insert(b,v2)
        final = "".join(w)
        res = super().blankRes()
        res["output"].append("Here's one! %s"%final)
        return res
    def listPoints(self, message, level):
        if level < self.scoreEditLevel:
            return
        l = self.db.scoreListTypes(message.channel.id)
        res = super().blankRes()
        result = []
        if len(l) == 0:
            result.append("I'm not keeping track of any points yet!")
        else:
            result.append("Here's all the score types i'm keeping track off!")
            for line in l:
                result.append(":::> **"+line+"**")
        res["output"].append("\n".join(result))
        return res

    def getPoints(self, message, level):
        if level < self.scoreEditLevel:
            return

        s = re.search("hodge podge summerise (.*) points\s*$",self.clean(message.content))
        scoreType = self.shallowClean(s.group(1))
        l = self.db.getAllScores(message.channel.id, scoreType)
        res = super().blankRes()
        result = []
        server = message.channel.server
        if len(l) == 0:
            result.append("Nobody has any points yet!")
        else:
            result.append("Here's all the "+scoreType+" scores!")
            for line in l:
                p = find(lambda m: m.id == line[0], server.members)
                result.append(":::> **"+p.name+"** : "+line[1])
        res["output"].append("\n".join(result))
        return res

    def shallowClean(self, t):
        return t.strip().lower()

    def clean(self, t):
        m = t.lower()
        m = re.sub(r'\s+',' ',m)
        m = re.sub(r'[\,\.\?\;\:\%\#\@\!\^\&\*\+\-\+\_\~\']','',m)
        m = m.strip()
        return m

    def trigger(self, message, requestLevel):
        res = super().blankRes()
        original = message.content;
        m = self.clean(message.content)
        for command in self.commands:
            if re.search(command[0],m):
                res = command[1](message,requestLevel)
=======
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
>>>>>>> 9dc43570a5b796e49e1942c78d9499f802eb8a02
        return res

import re
from functools import reduce

def preprocess(s):
    s = re.sub("<@!431280056468242435>","!hp",s)
    s = re.sub("hodge\s*podge","!hp",s,flags=re.IGNORECASE)
    return s

class Context:
    def __init__(self, message):
        self.message = preprocess(message.content)
        self.server = message.server.id
        self.location = message.channel.id
        self._message = message
        self.groups = None
        self.match = False
    def test(self, *patterns):
        s = self.message
        r = [re.search("!hp "+p,s,flags=re.IGNORECASE) != None for p in patterns]
        return reduce(lambda x,y: x or y,r)
    def apply(self, pattern):
        self.match = False
        pattern = "!hp {}".format(pattern)
        m = re.search(pattern,self.message,flags=re.IGNORECASE)
        if m:
            self.groups = m.groups()
            self.raw = m.group(0)
            self.match = True
    async def apply_chain(self, chain):
        for e in chain:
            self.apply(e[0])
            if self.match:
                return await e[1](self.groups,self)

    def group(self, n):
        return self.groups[n]

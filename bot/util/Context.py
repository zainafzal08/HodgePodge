import re
from functools import reduce

def preprocess(s):
    s = re.sub("<@!431280056468242435>","!hp",s)
    s = re.sub("hodge\s+podge","!hp",s,flags=re.IGNORECASE)
    return s

class Context:
    def __init__(self. message):
        self.message = preprocess(message.content)
        self.location = message.channel
        self._message = message
    def test(*patterns):
        s = this.message
        r = [re.search("!hp "+p,s,flags=re.IGNORECASE) != None for p in patterns]
        return reduce(lambda x,y: x or y,r)

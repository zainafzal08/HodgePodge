import re
from functools import reduce

def trigger(s,*patterns):
    r = [re.search("!hp "+p,s,flags=re.IGNORECASE) != None for p in patterns]
    return reduce(lambda x,y: x or y,r)

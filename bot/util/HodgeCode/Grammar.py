def find(l,i):
    try:
        return l.index(i)
    except:
        return -1

def l_filter(f,l):
    return list(filter(f,l))

class Grammar:
    def __init__(self):
        self.digits = [str(i) for i in range(0,10)]
        self.transformations = {
          "E": ["T Q"],
          "Q": ["+ T Q","- T Q","e"],
          "T": ["F R"],
          "R": ["* F R","/ F R","e"],
          "F": ["N","( E )"],
          "N": ["D I P"],
          "I": ["D I","e"],
          "P": [". I","e"],
          "D": self.digits
        }
        self.root = "E"
        self.ignore = [" ","\t","\n"]
        self.terminals = ["+","-","(",")",".","*","/"] + self.digits
        self.calculate_sets()

    def calculate_sets(self):
        self.select_set = {}
        self.first_set = {}
        self.follow_set = {}
        for key in self.transformations.keys():
            self.first_set[key] = self.get_first_set(key)
        for key in self.transformations.keys():
            eps = "e" in self.transformations[key]
            self.follow_set[key] = self.get_follow_set(key) if eps else set()
            self.select_set[key] = self.first_set[key] | self.follow_set[key]
    def get_first_set(self,t):
        if t == "e":
            return set()
        if t in self.terminals:
            return set([t])
        s = set()
        for option in self.transformations[t]:
            f = option.split(" ")[0]
            if f in self.terminals:
                s.add(f)
            else:
                s |= self.get_first_set(f)
        return s

    def find_trans(self, trans, t):
        r = []
        for o in self.transformations[trans]:
            r.append((o.split(" "),len(o.split(" "))-1,find(o.split(" "),t)))
        return l_filter(lambda x: x[2] != -1,r)

    def epislon_trans(self, t):
        if t in self.terminals:
            return False
        return "e" in self.transformations[t]

    def grab_until_epislon(self, l, i, s):
        while i < len(l)-1 and self.epislon_trans(l[i]):
            s |= self.first_set[l[i]]
            i+=1
        s |= self.first_set[l[i]]
        return i == len(l)-1;

    def process_matches(self, trans, t, matches, s):
        for match in matches:
            if match[2] == match[1]:
                s |= self.first_set[match[0][-1]]
                s |= self.get_follow_set(trans) if trans != t else set()
            elif match[0][match[2]+1] in self.terminals:
                s.add(match[0][match[2]+1])
            elif self.epislon_trans(match[0][match[2]+1]):
                r = self.grab_until_epislon(match[0],match[2]+1,s)
                s |= self.get_follow_set(trans) if r and trans != t else set()
            else:
                s |= self.first_set[match[0][match[2]+1]]

    def get_follow_set(self,t):
        s = set()
        if t == "e":
            return s
        if t in self.terminals:
            return s
        for trans in self.transformations:
            matches = self.find_trans(trans,t)
            self.process_matches(trans, t, matches, s)
        return s

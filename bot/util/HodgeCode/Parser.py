class Scanner:
    def __init__(self, raw):
        self.raw = raw
        self.pos = 0
    def done(self):
        return self.pos >= len(self.raw)
    def next(self):
        if self.done():
            return None
        self.pos+=1
        return self.raw[self.pos-1]
    def peek(self):
        if self.done():
            return None
        return self.raw[self.pos]

class Node:
    def __init__(self, title):
        self.title = title
        self.children = []
        self.parent = None
        self.length = 0
    def kid(self, t):
        n = Node(t)
        n.parent = self
        self.children.append(n)

class Parser:
    def __init__(self, grammar, text):
        self.grammar = grammar
        for ignore in self.grammar.ignore:
            text = text.replace(ignore,"")
        self.scanner = Scanner(text)
        self.root = Node("E")
        self.curr = self.root
        self.parse("E")
    def ascend(self):
        self.curr = self.curr.parent
    def decend(self):
        self.curr = self.curr.children[-1]
    def pick(self, lh, options):
        for option in options:
            c = option.split(" ")[0]
            if c in self.grammar.terminals and c == lh:
                return option
            elif c in self.grammar.terminals:
                continue
            elif lh in self.grammar.first_set[c]:
                return option
        return None
    def parse(self, t):
        if t in self.grammar.terminals:
            self.scanner.next()
            return
        lh = self.scanner.peek()
        if lh == None:
            if "e" in self.grammar.transformations[t]:
                self.curr.kid("e")
                return
            raise Exception("Unexpected end of input")
        if lh in self.grammar.first_set[t]:
            trans = self.pick(lh, self.grammar.transformations[t])
            for t in trans.split(" "):
                self.curr.kid(t)
                self.decend()
                self.parse(t)
                self.ascend()
        elif lh in self.grammar.follow_set[t]:
            self.curr.kid("e")
        else:
            raise Exception("Unexpeted token '{}'".format(lh))

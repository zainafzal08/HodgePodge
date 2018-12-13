class Emitter:
    def __init__(self, g):
        self.grammar = g
        self.code_mem = []
        self.node_map = {
          "E": self.emit_E,
          "Q": self.emit_Q,
          "T": self.emit_T,
          "R": self.emit_R,
          "F": self.emit_F,
          "N": self.emit_N,
          "I": self.emit_I,
          "P": self.emit_P,
          "D": self.emit_D
        }
    def code(self, l):
        if type(l) is str:
            self.code_mem.append(l)
        elif type(l) is list:
            self.code_mem += l
        else:
            raise Exception("Expected Instance of Str or List")

    def emit(self, r):
        self.node_map[r.title](r)
    def emit_E(self, r):
        self.emit(r.children[0])
        self.emit(r.children[1])
    def emit_Q(self, r):
        if (len(r.children) == 1):
            return
        self.emit(r.children[1])
        self.emit(r.children[2])
        self.code("ADD") if r.children[0].title == "+" else self.code("SUB")
    def emit_T(self, r):
        self.emit(r.children[0])
        self.emit(r.children[1])
    def emit_R(self, r):
        if len(r.children) == 1:
            return
        self.emit(r.children[1])
        self.emit(r.children[2])
        self.code("MULT") if r.children[0].title == "*" else self.code("DIV")
    def emit_F(self, r):
        if len(r.children) == 1:
            self.emit(r.children[0])
        else:
            self.emit(r.children[1])
    def emit_N(self, r):
        self.emit(r.children[1])
        self.emit(r.children[0])
        self.code(["PUSH 10"]*r.children[1].length)
        self.code(["MULT"]*r.children[1].length)
        self.code("ADD")
        self.emit(r.children[2])
        self.code(["PUSH 10"]*r.children[2].length)
        self.code(["DIV"]*r.children[2].length)
        self.code("ADD")
    def emit_I(self, r):
        if len(r.children) == 1:
            self.code("PUSH 0")
            return
        self.emit(r.children[1])
        self.emit(r.children[0])
        self.code(["PUSH 10"]*r.children[1].length)
        self.code(["MULT"]*r.children[1].length)
        self.code("ADD")
        r.length = r.children[1].length+1
    def emit_P(self, r):
        if len(r.children) == 1:
            self.code("PUSH 0")
            return
        self.emit(r.children[1])
        r.length = r.children[1].length
    def emit_D(self, r):
        self.code("PUSH "+r.children[0].title)

class Stack:
    def __init__(self):
        self.data = []
    def push(self, v):
        self.data.append(float(v))
    def pop(self):
        return self.data.pop()

class VM:
    def __init__(self):
        self.stack = Stack()
    def run(self, code):
        for l in code:
            i = l.split(" ")[0]
            args = l.split(" ")[1:]
            if i == "PUSH":
                self.stack.push(args[0])
            if i == "ADD":
                self.stack.push(self.stack.pop() + self.stack.pop())
            if i == "SUB":
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.push(a - b)
            if i == "MULT":
                self.stack.push(self.stack.pop() * self.stack.pop())
            if i == "DIV":
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.push(a / b)

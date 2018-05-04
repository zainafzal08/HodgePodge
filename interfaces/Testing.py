import threading
from utils.State import State

class Testing(threading.Thread):
    def __init__(self, threadID, boy):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = "Testing"
        self.boy = boy
        self.me = "testboy"
        self.location = "testingChat"

    def runCmd(self, raw):
        cmd = raw.split(" ")[0]
        args = raw.split(" ")[1:]
        if cmd == ".quit":
            break
        elif cmd == ".location":
            self.location = args[0]
        elif cmd == ".user":
            self.me = args[0]

    def run(self):
        while True:
            raw = input("> ")
            if raw[0] == ".":
                self.runCmd(raw)
            else:
                state = State(self.me)
                self.boy.talk(state,raw)

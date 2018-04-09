import sys
import re

class TestInterface():
    def __init__(self,boy):
        self.boy = boy
        self.level = 0
        self.done = False
        self.running = False
        self.location = "testingTerminal"
        self.cmds = [
            ('role (\w+)', self.addRole, True,"Roles Updated"),
            ('quit', self.exit, False,"Goodbye"),
            ('location (\w+)',self.updateLocation,True,"Location Updated")
        ]
        self.cmdTrigger = "\\"
        self.me = User("TesterBoy","TesterBoy")
        self.members = [self.me]
    def run(self):
        print("[ Launching Test Interface...")
        print("[ Ready!")
        self.running = True
        l = self.getLine()
        while self.running:
            if l[0] == self.cmdTrigger:
                r = self.interfaceCommands(l[1:])
                print("[ %s"%r)
            else:
                res = self.boy.talk(l,self.me,self.location, self.members)
                if res:
                    print("@ %s >> %s"%(res.getTextTarget(), res.getTextMsg()))
            if self.running:
                l = self.getLine()
    def prompt(self):
        prmpt = "@ %s > "%self.location
        sys.stdout.write(prmpt)
        l = input()
        return l

    def getLine(self):
        try:
            l = self.prompt()
            return l
        except():
            self.running = False
            return None

    def addRole(self, r):
        self.me.addRole(r)

    def updateLocation(self, loc):
        if loc:
            self.location = loc

    def exit(self):
        self.running = False
        return

    def interfaceCommands(self, txt):
        for cmd in self.cmds:
            s = re.search(cmd[0],txt)
            if s:
                if cmd[2]:
                    cmd[1](s.group(1))
                else:
                    cmd[1]()
                return cmd[3]
        return "Illegal Command"

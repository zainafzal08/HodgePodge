import time

class Role():
    def __init__(self, display):
        #TODO: Replace this with a secret key hash of the time.
        self.id = str(int(time.time()))
        self.display = display
    def getId(self):
        return self.id
    def getDisplay(self):
        return self.display

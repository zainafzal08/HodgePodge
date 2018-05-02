import threading

class Testing(threading.Thread):
    def __init__(self, threadID, boy):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = "Testing"
        self.boy = boy
    def run(self):
        

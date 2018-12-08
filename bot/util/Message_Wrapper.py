class Message_Wrapper:
    def __init__(self, m, **kargs):
        self.content = m
        self.channel = kargs.get("me","testing-terminal")

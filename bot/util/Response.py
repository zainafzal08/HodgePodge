class Response:
    def __init__(self, m, **kargs):
        self.location = kargs.get("location",None)
        self.content = m

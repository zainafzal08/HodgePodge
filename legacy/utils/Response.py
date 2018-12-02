class Response():
    def __init__(self):
        self.text = {}
    def text_responce(self, msg, target, type):
        self.text["msg"] = msg
        self.text["target"] = target
        self.text["type"] = type
    def get_text_target(self):
        return self.text.get("target",None)
    def get_text_msg(self):
        t = self.text.get("msg",None)
        if t and len(t) > 2000:
            return "_bzzt_ Response too big to display, use web interface."
        return t

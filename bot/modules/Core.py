from util.Response import Response
from util.matching import trigger

class Core:
    def __init__(self):
        self.doc_link = "http://zainafzal08.github.io/HodgePodge"

    async def message(self, m):
        if trigger(m,"help","show documentation","docs","how do i.*"):
            msg = "I have a nice list of what i can do at {}".format(self.doc_link)
            return Response(msg)

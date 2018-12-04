from util.Response import Response

class Core:
    def __init__(self):
        self.doc_link = "http://zainafzal08.github.io/HodgePodge"

    async def message(self, context):
        if context.test("help","show documentation","docs","how do i.*"):
            msg = "I have a nice list of what i can do at {}".format(self.doc_link)
            return Response(msg)
        if context.test(m,"i love you"):
            msg = "i love you too"
            return Response(msg)

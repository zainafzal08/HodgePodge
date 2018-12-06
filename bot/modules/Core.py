from util.Response import Response
import aiohttp

class Core:
    def __init__(self):
        self.doc_link = "http://zainafzal08.github.io/HodgePodge/docs.html"

    async def post_env_var(self, key, value):
        # aiohttp magic here lol good luck fuck face
        print("{}={}".format(key,value))
        pass

    async def message(self, context):
        if context.test("help","show documentation","docs","how do i.*"):
            msg = "I have a nice list of what i can do at {}".format(self.doc_link)
            return Response(msg)
        if context.test("i love you"):
            msg = "i love you too"
            return Response(msg)
        context.apply("set ([\w_]+) to (.*)")
        if context.match:
            await self.post_env_var(self,context.group(0),context.group(1))
            return Response("Got it!")

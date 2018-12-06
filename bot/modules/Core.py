from util.Response import Response
from logger import core_module_logger
import os
import aiohttp

class Core:
    def __init__(self):
        self.doc_link = "http://zainafzal08.github.io/HodgePodge/docs.html"
        self.api_url = "http://127.0.0.1:8000/"
    def url(self, *args):
        return self.api_url + "/".join(args)

    async def post_env_var(self, server, key, value):
        options = {}
        options["json"] = {"key":key,"value":value}
        options["headers"] = {"Authoriziation": "token {}".format(os.environ['auth_key'])}
        async with aiohttp.ClientSession() as session:
            async with session.post(url("server",server,"env"),**options) as resp:
                l = "POST {} ({}={}) - {}".format(url("server",server,"env"),key,value,resp.status)
                core_module_logger(l)

    async def message(self, context):
        if context.test("help","show documentation","docs","how do i.*"):
            msg = "I have a nice list of what i can do at {}".format(self.doc_link)
            return Response(msg)
        if context.test("i love you"):
            msg = "i love you too"
            return Response(msg)
        context.apply("set ([\w_]+) to (.*)")
        if context.match:
            await self.post_env_var(self,context.location,context.group(0),context.group(1))
            return Response("Got it!")

from util.Response import Response
from loggers import core_module_logger
import os
import aiohttp
import json

class Core:
    def __init__(self):
        self.doc_link = "http://zainafzal08.github.io/HodgePodge/docs.html"
        self.api_url = "http://127.0.0.1:8000/"
    def url(self, *args):
        return self.api_url + "/".join(args)

    async def post_env_var(self, server, key, value):
        options = {}
        options["data"] = json.dumps({"key":key,"value":value})
        options["headers"] = {
            "Authorization": "token {}".format(os.environ['auth_key']),
            "Content-Type": "application/json"
        }
        async with aiohttp.ClientSession() as session:
            async with session.put(self.url("server",server,"env"),**options) as resp:
                l = "PUT {} ({}={}) - {}".format(self.url("server",server,"env"),key,value,resp.status)
                core_module_logger.info(l)

    async def get_env_var(self, server, key):
        # do fancy stuff to get a object
        options = {}
        options["headers"] = {"Authorization": "token {}".format(os.environ['auth_key'])}
        o = {}
        async with aiohttp.ClientSession() as session:
            async with session.get(self.url("server",server,"env"),**options) as resp:
                l = "GET {} - {}".format(self.url("server",server,"env"), resp.status)
                core_module_logger.info(l)
                o = json.loads(await resp.text())
        return o.get(key,None)

    async def message(self, context):
        if context.test("help","show documentation","docs","how do i.*"):
            msg = "I have a nice list of what i can do at {}".format(self.doc_link)
            return Response(msg)
        if context.test("i love you"):
            msg = "i love you too"
            return Response(msg)
        context.apply("set ([\w_]+) to (.*)")
        if context.match:
            await self.post_env_var(context.server,context.group(0),context.group(1))
            return Response("Got it!")
        context.apply("reveal ([\w_]+)")
        if context.match:
            v = await self.get_env_var(context.server,context.group(0))
            if v == None:
                return Response("No SEV by that name exists!")
            return Response("{} = {}".format(context.group(0),v))

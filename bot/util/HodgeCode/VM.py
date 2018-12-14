import os
import math
import os
import aiohttp
import json

class Stack:
    def __init__(self):
        self.data = []
    def push(self, v):
        self.data.append(float(v))
    def pop(self):
        return self.data.pop()

class VM:
    def __init__(self, symbol_table):
        self.symbol_table = symbol_table
        self.stack = Stack()
        self.api_url = "http://127.0.0.1:8000/"
    def url(self, *args):
        return self.api_url + "/".join(args)
    async def get_env_var(self, server, key):
        # do fancy stuff to get a object
        options = {}
        options["headers"] = {"Authorization": "token {}".format(os.environ['auth_key'])}
        o = {}
        async with aiohttp.ClientSession() as session:
            async with session.get(self.url("server",server,"env"),**options) as resp:
                o = json.loads(await resp.text())
        return o.get(key,None)
    def random_num(self, type):
        r = int.from_bytes(os.urandom(2),byteorder='little')/(2**16)
        r = math.ceil(r*type)
        return r
    async def run(self, code, server):
        for l in code:
            i = l.split(" ")[0]
            args = l.split(" ")[1:]
            if i == "PUSH":
                self.stack.push(args[0])
            if i == "ADD":
                self.stack.push(self.stack.pop() + self.stack.pop())
            if i == "SUB":
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.push(a - b)
            if i == "MULT":
                self.stack.push(self.stack.pop() * self.stack.pop())
            if i == "DIV":
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.push(a / b)
            if i == "ROLL":
                t = self.stack.pop()
                if t < 2 or t > 10000:
                    raise Exception("instr ROLL can not roll a dice with {} faces!".format(t))
                self.stack.push(self.random_num(t))
            if i == "LDV":
                v = int(self.stack.pop())
                v = self.symbol_table[v]
                self.stack.push(await self.get_env_var(server, v))

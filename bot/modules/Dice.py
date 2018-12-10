from util.Response import Response
from util.misc import lmap
import math
import os
from loggers import dice_module_logger
from functools import reduce
import aiohttp
import json
class Dice:
    def __init__(self):
        self.api_url = "http://127.0.0.1:8000/"
    def random_num(self, type):
        r = int.from_bytes(os.urandom(2),byteorder='little')/(2**16)
        r = math.ceil(r*type)
        return r
    def url(self, *args):
        return self.api_url + "/".join(args)
    async def get_env_var(self, server, key):
        # do fancy stuff to get a object
        options = {}
        options["headers"] = {"Authorization": "token {}".format(os.environ['auth_key'])}
        o = {}
        async with aiohttp.ClientSession() as session:
            async with session.get(self.url("server",server,"env"),**options) as resp:
                l = "GET {} - {}".format(self.url("server",server,"env"), resp.status)
                dice_module_logger.info(l)
                o = json.loads(await resp.text())

        if ("critical_hit_msg" not in o):
            o["critical_hit_msg"] = "Nice!"
        if ("critical_miss_msg" not in o):
            o["critical_miss_msg"] = "oof."
        return o.get(key,None)

    async def save_roll(self, server, value):
        options = {}
        key = "last_roll"
        options["data"] = json.dumps({"key":key,"value":value})
        options["headers"] = {
            "Authorization": "token {}".format(os.environ['auth_key']),
            "Content-Type": "application/json"
        }
        async with aiohttp.ClientSession() as session:
            async with session.put(self.url("server",server,"env"),**options) as resp:
                l = "PUT {} ({}={}) - {}".format(self.url("server",server,"env"),key,value,resp.status)
                dice_module_logger.info(l)

    async def multi_roll(self, grps, context):
        await self.save_roll(context.location,context.raw)
        dice_num = int(grps[0])
        dice_type = int(grps[1])
        mod,val=[None,None]
        if len(grps) > 2:
            mod,val = grps[2:]
            val = int(val)
            if abs(val) > 100000:
                return Response("Bit of a intense modifier, not sure i can handle a number like that. Sorry!")
        if dice_type < 2 or dice_type > 10000:
            return Response("How can you even have that many faces on a dice? Pick a reasonable dice please!")
        if dice_num < 1 or dice_num > 10000:
            return Response("That is not a amount of dice i can roll, be reasonable.")

        rolls = [self.random_num(dice_type) for _ in range(dice_num)]
        total = sum(rolls)
        rolls = lmap(lambda x: str(x),rolls)
        if mod == "+" or mod == "-":
            total = total + val if mod == "+" else total - val
            rolls = "({})[{}{}]".format(",".join(rolls),mod,val)
        elif mod == "++" or mod == "--":
            total = total + val*dice_num if mod[0] == "+" else total - val*dice_num
            rolls = list(map(lambda x: "{}[{}{}]".format(x,mod[0],val),rolls))
            rolls = "({})".format(",".join(rolls))
        else:
            rolls = "({})".format(",".join(rolls))
        if dice_num > 20:
            return Response("I got {}!".format(total))
        return Response("I got {}! The breakdown was {}".format(total,rolls))

    async def single_roll(self, grps, context):
        await self.save_roll(context.location,context.raw)
        dice_type = int(grps[0])
        mod,val=[None,None]
        if len(grps) > 1:
            mod,val = grps[1:]
            val = int(val)
            if abs(val) > 100000:
                return Response("Bit of a intense modifier, not sure i can handle a number like that. Sorry!")

        if dice_type < 2 or dice_type > 10000:
            return Response("How can you even have that many faces on a dice? Pick a reasonable dice please!")

        hit = await self.get_env_var(context.location, "critical_hit_msg")
        miss = await self.get_env_var(context.location, "critical_miss_msg")
        og_roll = self.random_num(int(dice_type))
        roll = og_roll
        if (mod != None and val != None):
            roll = roll + val if mod == "+" else roll - val
        prefix = "{} ".format(miss) if (og_roll == 1) else ""
        postfix = " {}".format(hit) if (og_roll == dice_type) else ""
        modStr = " [{}{}{}]".format(og_roll,mod,val) if mod != None and val != None else ""
        msg = "{}I got {}{}!{}".format(prefix,roll,modStr,postfix)
        return Response(msg)

    async def message(self, context):
        if context.message == "!hp reroll":
            lr = await self.get_env_var(context.location, "last_roll")
            if lr == None:
                return Response("I don't know what you last rolled! Sorry!")
            context.message = lr
        chain = [
            (".*roll[^\d]*(\d+).*d(\d+)[^\+\-]*([+\-][+\-]?)\s*(\d+)",self.multi_roll),
            (".*roll[^\d]*(\d+).*d(\d+)",self.multi_roll),
            (".*roll.*d(\d+).*([+\-])\s*(\d+)",self.single_roll),
            (".*roll.*d(\d+)",self.single_roll)
        ]
        return await context.apply_chain(chain)

from util.Response import Response
from util.misc import lmap
import math
import os
from loggers import dice_module_logger
from functools import reduce

class Dice:
    def __init__(self):
        pass
    def random_num(self, type):
        r = int.from_bytes(os.urandom(2),byteorder='little')/(2**16)
        r = math.ceil(r*type)
        return r
    async def get_env_var(self, server, key):
        # do fancy stuff to get a object
        options = {}
        options["headers"] = {"Authoriziation": "token {}".format(os.environ['auth_key'])}
        o = {}
        async with aiohttp.ClientSession() as session:
            async with session.get(url("server",server,"env"),**options) as resp:
                l = "GET {} - {}".format(url("server",server,"env"), resp.status)
                dice_module_logger(l)
                o = await resp.json()

        if ("critial_hit_msg" not in o):
            o["critial_hit_msg"] = "Nice!"
        if ("critial_miss_msg" not in o):
            o["critial_miss_msg"] = "oof."
        return o[key]

    async def multi_roll(self, grps, context):
        dice_num = grps[0]
        dice_type = grps[1]
        mod,val=[None,None]
        if len(grps) > 2:
            mod,val = grps[2:]
        dice_num = int(dice_num)
        dice_type = int(dice_num)
        val = int(val) if val else None

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
        return Response("I got {}! The breakdown was {}".format(total,rolls))

    async def single_roll(self, grps, context):
        dice_type = grps[0]
        mod,val=[None,None]
        if len(grps) > 1:
            mod,val = grps[1:]
        dice_type = int(dice_type)
        val = int(val) if val else None

        hit = await self.get_env_var(context.location, "critial_hit_msg")
        miss = await self.get_env_var(context.location, "critial_miss_msg")
        og_roll = self.random_num(int(dice_type))
        roll = og_roll
        if (mod != None and val != None):
            roll = roll + val if mod == "+" else roll - val
        prefix = "{} ".format(miss) if (roll == 1) else ""
        postfix = " {}".format(hit) if (roll == dice_type) else ""
        modStr = " [{}{}{}]".format(og_roll,mod,val) if mod != None and val != None else ""
        msg = "{}I got {}{}!{}".format(prefix,roll,modStr,postfix)
        return Response(msg)

    async def message(self, context):
        chain = [
            (".*roll.*(\d+).*d(\d+)[^\+\-]*([+\-][+\-]?)\s*(\d+)",self.multi_roll),
            (".*roll.*(\d+).*d(\d+)",self.multi_roll),
            (".*roll.*d(\d+).*([+\-])\s*(\d+)",self.single_roll),
            (".*roll.*d(\d+)",self.single_roll)
        ]
        return await context.apply_chain(chain)

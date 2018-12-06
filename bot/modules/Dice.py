from util.Response import Response
import math
import os
from functools import reduce

class Dice:
    def __init__(self):
        pass
    def random_num(self, type):
        r = int.from_bytes(os.urandom(2),byteorder='little')/(2**16)
        r = math.ceil(r*type)
        return r
    async def get_env_var(self, key):
        if(key == "critial_hit_msg"):
            return "Nice!"
        if(key == "critial_miss_msg"):
            return "oof."
    def multi_roll(self, dice_num,dice_type,mod,val):
        dice_num = int(dice_num)
        if val:
            val = int(val)
        rolls = [self.random_num(int(dice_type)) for _ in range(dice_num)]
        total = sum(rolls)
        rolls = list(map(lambda x: str(x),rolls))
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

    async def single_roll(self, dice_type,mod,val):
        if val:
            val = int(val)
        hit = await self.get_env_var("critial_hit_msg")
        miss = await self.get_env_var("critial_miss_msg")
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
        context.apply("roll.*(\d+).*d(\d+)[^\+\-]*([+\-][+\-]?)\s*(\d+)")
        if context.match:
            g = list(context.groups)
            return self.multi_roll(g[0],g[1],g[2],g[3])
        context.apply("roll.*(\d+).*d(\d+)")
        if context.match:
            g = list(context.groups)
            return self.multi_roll(g[0],g[1],None,None)
        context.apply("roll.*d(\d+).*([+\-])\s*(\d+)")
        if context.match:
            return await self.single_roll(context.group(1),context.group(2),context.group(3))
        context.apply("roll.*d(\d+)")
        if context.match:
            return await self.single_roll(context.group(1),None,None)

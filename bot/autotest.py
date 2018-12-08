import os
import re
from loggers import hodge_logger
from util.Context import Context
from util.Message_Wrapper import Message_Wrapper
from modules.Core import Core
from modules.Dice import Dice
import asyncio
import sys
from loggers import silence

call_chain = [Dice(),Core()]

async def simulate_message(message):
    context = Context(Message_Wrapper(message,me="btf"))
    for module in call_chain:
        r = await module.message(context)
        if r == None:
            continue
        location = r.location
        if not location:
            location = context.location
        print("[{}] {}".format(location, r.content))
        break

async def run():
    silence()
    await simulate_message(sys.argv[1])

loop = asyncio.get_event_loop()
loop.run_until_complete(run())

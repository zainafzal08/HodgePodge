import os
import re
from loggers import hodge_logger
from util.Context import Context
from util.Message_Wrapper import Message_Wrapper
from modules.Core import Core
from modules.Dice import Dice
import asyncio

call_chain = [Dice(),Core()]

async def simulate_message(message):
    context = Context(Message_Wrapper(message))
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
    hodge_logger.info("Running Testing Interface v.1.0!")
    hodge_logger.info("Launching Bot")
    i = input("> ")
    while (i != "!hp q"):
        await simulate_message(i)
        i = input("> ")


loop = asyncio.get_event_loop()
loop.run_until_complete(run())

import discord
import os
import re
from loggers import hodge_logger
from util.Context import Context
from modules.Core import Core
from modules.Dice import Dice

client = discord.Client()
call_chain = [Dice(),Core()]

@client.event
async def on_ready():
    status = 'Connected to discord as {}[{}]'.format(client.user.name,client.user.id)
    hodge_logger.info(status)

@client.event
async def on_message(message):
    # ignore bots
    if (message.author.bot):
        return
    context = Context(message)
    for module in call_chain:
        r = await module.message(context)
        if r == None:
            continue
        location = r.location
        if not location:
            location = message.channel
        await client.send_message(location, r.content)
        break

def run():
    hodge_logger.info("Launching Bot")
    client.run(os.environ['bot_token'])
    client.close()

# i guess run
run()

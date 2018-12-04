import discord
import os
import re
from loggers import hodge_logger
from modules.Core import Core

client = discord.Client()
call_chain = [Core()]

def preprocess(s):
    s = re.sub("<@!431280056468242435>","!hp",s)
    s = re.sub("hodge\s+podge","!hp",s,flags=re.IGNORECASE)
    return s

@client.event
async def on_ready():
    status = 'Connected to discord as {}[{}]'.format(client.user.name,client.user.id)
    hodge_logger.info(status)

@client.event
async def on_message(message):
    # ignore bots
    if (message.author.bot):
        return
    # preprocess
    m = preprocess(message.content)
    for module in call_chain:
        await module.message(m)

def run():
    hodge_logger.info("Launching Bot")
    client.run(os.environ['bot_token'])
    client.close()

# i guess run
run()

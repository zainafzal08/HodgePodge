import discord
import os
from loggers import hodge_logger

client = discord.Client()


@client.event
async def on_ready():
    status = 'Connected to discord as {}[{}]'.format(client.user.name,client.user.id)
    hodge_logger.info(status)

@client.event
async def on_message(message):
    # ignore bots
    if (message.author.bot):
        return


def run():
    hodge_logger.info("Launching Bot")
    client.run(os.environ['BOT_TOKEN'])
    client.close()

# i guess run
run()

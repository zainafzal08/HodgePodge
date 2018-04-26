import discord
from discord.utils import find
from utils.User import User

client = discord.Client()

def run(boyRef,token):
    client.run(token)
    client.close()

def getChannel(id):
    all = client.get_all_channels()
    target = [c for c in all if c.id == id]
    if len(target) > 0:
        return target[0]
    return None

@client.event
async def on_ready():
    print('Connected to discord as %s[%s]'%(client.user.name,client.user.id))

@client.event
async def on_message(message):
    # ignore bots
    if(message.author.bot):
        return

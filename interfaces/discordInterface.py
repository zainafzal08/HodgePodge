import discord
from discord.utils import find
from utils.State import State

client = discord.Client()
boy = None

def run(boyRef,token):
    global boy
    boy = boyRef
    client.run(token)
    client.close()

def get_channel(id):
    all = client.get_all_channels()
    target = [c for c in all if c.id == id]
    if len(target) > 0:
        return target[0]
    return None

def get_user(msg, usr):
    admin = usr.permissions_in(msg.channel).administrator
    tgs = [x.name for x in usr.roles if x.name.isalnum()]
    return (usr.id,tgs,admin,usr.name)

@client.event
async def on_ready():
    print('Connected to discord as %s[%s]'%(client.user.name,client.user.id))

@client.event
async def on_message(message):
    # ignore bots
    if(message.author.bot):
        return

    # get basics
    location = message.channel.id
    me = get_user(message, find(lambda x: x.name == "Hodge-Podge",message.server.members))
    q = message.content
    author = get_user(message, message.author)
    members = [get_user(message, member) for member in message.server.members]
    members.remove(me)

    # talk
    state = State(author, members, location)
    r = boy.talk(state, q)

    # respond
    if not r:
        return
    msg = r.get_text_msg()
    channel = get_channel(r.get_text_target())
    if msg and channel:
        await client.send_message(channel, msg)

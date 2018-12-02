import discord
from discord.utils import find
from utils.State import State
from utils.User import User
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
    u = User("Discord",usr.id)
    u.external_admin = usr.permissions_in(msg.channel).administrator
    u.external_tags = set([x.name for x in usr.roles if x.name.isalnum()])
    u.external_name = usr.name
    return u

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

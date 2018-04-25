import discord
from discord.utils import find
from utils.User import User

client = discord.Client()
boy = None

def run(boyRef,token):
    global boy
    boy = boyRef
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
    global boy
    # ignore bots
    if(message.author.bot):
        return
    location = message.channel.id
    raw = message.content
    roles = list(map(lambda x: x.name, message.author.roles))
    author = User(message.author.id,message.author.name)
    author.addRoles(roles)
    members=[]
    myself = find(lambda x: x.name == "Hodge-Podge",message.server.members).id
    for member in message.server.members:
        if member.id == myself:
            continue
        members.append(User(member.id,"<@%s>"%member.id))

    res = boy.talk(raw,author,location,members)
    if not res:
        return
    msg = res.getTextMsg()
    if not msg:
        return
    channel = getChannel(res.getTextTarget())
    if not channel:
        return
    await client.send_message(channel, msg)

import interfaces.discordInterface
from HodgePodge import HodgePodge
from modules.Game import Game
from modules.Utility import Utility
from modules.UserTools import UserTools
import os

# set up our boy :3
db = os.environ['DATABASE_URL']
boy = HodgePodge(db)
boy.attach_module(Game())
boy.attach_module(Utility())
boy.attach_module(UserTools())
tkn = os.environ['BOT_TOKEN']
interfaces.discordInterface.run(boy,tkn)

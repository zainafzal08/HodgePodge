from interfaces import discordInterface
from HodgePodge import HodgePodge
from modules.Game import Game
from modules.Utility import Utility
import os

boy = HodgePodge(os.environ.get('DATABASE_URL',None))
boy.attachModule(Game())
boy.attachModule(Utility())

discordInterface.run(boy,os.environ.get('DISCORD_TOKEN'))

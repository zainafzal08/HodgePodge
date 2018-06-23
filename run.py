import interfaces.discordInterface
from HodgePodge import HodgePodge
from modules.Game import Game
from modules.Utility import Utility
from modules.UserTools import UserTools

# set up our boy :3
boy = HodgePodge('sqlite:///db/test.db')
boy.attach_module(Game())
boy.attach_module(Utility())
boy.attach_module(UserTools())

tkn = "NDMxMjgwMDU2NDY4MjQyNDM1.DgijaQ.o74HGWgf0rXkzbpQJ6Jou864gBE"
interfaces.discordInterface.run(boy,tkn)

from HodgePodge import HodgePodge
from modules.Game import Game
from modules.Utility import Utility
from modules.UserTools import UserTools

# set up our boy :3
boy = HodgePodge()
boy.attach_module(Game())
boy.attach_module(Utility())
boy.attach_module(UserTools())

# make a test state
state = State("1",[],"testing")
r = boy.talk(state, "hi")
print(r)

# end
boy.kill()

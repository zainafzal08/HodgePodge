from HodgePodge import HodgePodge
from modules.Game import Game
from modules.Utility import Utility
from modules.UserTools import UserTools
from utils.State import State

# set up our boy :3
boy = HodgePodge('sqlite:///db/test.db')
boy.attach_module(Game())
boy.attach_module(Utility())
boy.attach_module(UserTools())

# make a test state
state = State("1",[],"testing")
r = boy.talk(state, "hodge podge what my name")
print(r.get_text_msg())
r = boy.talk(state, "hodge podge call me fuckface")
print(r.get_text_msg())
r = boy.talk(state, "hodge podge what my name")
print(r.get_text_msg())
r = boy.talk(state, "hodge podge roll a fat d20 + 8")
print(r.get_text_msg())
r = boy.talk(state, "hodge podge calculate (5*10)/20")
print(r.get_text_msg())

# end
boy.kill()

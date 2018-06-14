from HodgePodge import HodgePodge
from modules.Game import Game
from modules.Utility import Utility
from modules.UserTools import UserTools
from utils.State import State

def say(r):
    if not r:
        print("> No Response")
    else:
        print(r.get_text_msg())
# set up our boy :3
boy = HodgePodge('sqlite:///db/test.db')
boy.attach_module(Game())
boy.attach_module(Utility())
boy.attach_module(UserTools())

# make a test state
me = ("1",["nerd"])
state = State(me,[],"testing")
r = boy.talk(state, "hodge podge what's my name")
say(r)
r = boy.talk(state, "hodge podge roll a fat d20 + 8")
say(r)
r = boy.talk(state, "hodge podge how do i use the utility module")
say(r)

# end
boy.kill()

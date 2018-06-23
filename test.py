from HodgePodge import HodgePodge
from modules.Game import Game
from modules.Utility import Utility
from modules.UserTools import UserTools
from utils.State import State

def say(r):
    if not r:
        print(">> No Response")
    else:
        print(r.get_text_msg())
# set up our boy :3
boy = HodgePodge('sqlite:///db/test.db')
boy.attach_module(Game())
boy.attach_module(Utility())
boy.attach_module(UserTools())

# make a test state
me = ("2",["nerd"],True)
friend = ("3",["gay"],False)
state = State(me,[friend],"testing")

q = input("> ")
while q != "q":
    r = boy.talk(state, q)
    say(r)
    q = input("> ")
# end
boy.kill()

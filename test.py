from HodgePodge import HodgePodge
from modules.Game import Game
from modules.Utility import Utility
from modules.UserTools import UserTools
from utils.State import State
from utils.User import User
import os

def say(r):
    if not r:
        print(">> No Response")
    else:
        print(r.get_text_msg())
# set up our boy :3
boy = HodgePodge(os.environ["DATABASE_URL"])
boy.attach_module(Game())
boy.attach_module(Utility())
boy.attach_module(UserTools())

# make a test state
me = User("Sandbox","1")
friend = User("Sandbox","2")
me.external_name = "Testing Boy"
friend.external_name = "Testing Friend"
state = State(me,[friend],"Testing_Terminal")

q = input("> ")
while q != "q":
    r = boy.talk(state, q)
    say(r)
    q = input("> ")

from interfaces.Testing import Testing
from HodgePodge import HodgePodge
from modules.Game import Game
from modules.Utility import Utility
from modules.UserTools import UserTools

# set up our boy :3
boy = HodgePodge()
boy.attachModule(Game())
boy.attachModule(Utility())
boy.attachModule(UserTools())

# init interfaces
interfaces = []
interfaces.append(Testing(1,boy))

# begin
for interface in interfaces:
    interface.start()
# await
for interface in interfaces:
    interface.join()
# end
boy.kill()

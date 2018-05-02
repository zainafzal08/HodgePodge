from interfaces.Testing import Testing
from HodgePodge import HodgePodge
from modules.Game import Game
from modules.Utility import Utility

# set up our boy :3
boy = HodgePodge()
boy.attachModule(Game())
boy.attachModule(Utility())

# set up the interfaces we want to run
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

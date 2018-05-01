from interfaces.Testing import Testing
from HodgePodge import HodgePodge

# set up the interfaces we want to run
boy = HodgePodge()
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

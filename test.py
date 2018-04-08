from interfaces.testInterface import TestInterface
from HodgePodge import HodgePodge
from modules.Game import Game
from modules.Utility import Utility

dbConn = "host='localhost' dbname='hpTest'"
boy = HodgePodge(dbConn)
boy.attachModule(Game())
boy.attachModule(Utility())
interface = TestInterface(boy)
interface.run()

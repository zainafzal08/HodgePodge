import falcon
from endpoints.User import User
from endpoints.Server import Env
from middleware.CORS import CORS
api = falcon.API(middleware=CORS())
api.add_route('/user/{discordId}', User())
api.add_route('/server/{serverId}/env', Env())

import falcon
from endpoints.User import User
api = falcon.API()
api.add_route('/user/{discordId}', User())

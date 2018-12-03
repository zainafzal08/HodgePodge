import falcon
from endpoints.User import User
from middleware.CORS import CORS
api = falcon.API(middleware=CORS())
api.add_route('/user/{discordId}', User())

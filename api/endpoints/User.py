import falcon
from db.DB import DB

class User(object):
    def __init__(self):
        self.db = DB()
        self.supportedAuthorizationTypes = ["token"]
    def authorize(self, req):
        if "AUTHORIZATION" not in req.headers:
            raise falcon.HTTPMissingHeader("Authorization")
        components = req.headers["AUTHORIZATION"].split(" ")
        if len(components) != 2:
            raise falcon.HTTPInvalidHeader("Expected <type> <credentials>", "Authorization")
        type,creds = components
        if type not in self.supportedAuthorizationTypes:
            raise falcon.HTTPInvalidHeader("Unsupported credential type", "Authorization")
        if creds not in self.db.authKeys():
            raise falcon.HTTPInvalidHeader("Invalid credentials", "Authorization")
    def on_post(self, req, resp, discordId):
        self.authorize(req)
        try:
            self.db.newUser(discordId)
        except:
            raise falcon.HTTPConflict(description="discordId already in use")

    def on_get(self, req, resp, discordId):
        self.authorize(req)
        try:
            resp.media = self.db.getUser(discordId)
        except:
            raise falcon.HTTPInvalidParam("Unknown user", "discordId")
    def on_put(self, req, resp, discordId):
        self.authorize(req)
        try:
            self.db.updateUser(discordId,req.media)
        except Exception as error:
            print(error)
            raise falcon.HTTPInvalidParam("Unknown user", "discordId")

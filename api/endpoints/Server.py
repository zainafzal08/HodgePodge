import falcon
from db.DB import DB

class Env(object):
    def __init__(self):
        self.db = DB()
        self.supportedAuthorizationTypes = ["token"]

    def enforce(j,**kargs):
        for k in kargs.keys():
            if k not in j:
                raise falcon.HTTPMissingParam(k)
            if j[k] != kargs[k]:
                raise falcon.HTTPInvalidParam("expected {} to be of type {}".format(k,kargs[k]),k)

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

    def on_get(self, req, resp, serverId):
        self.authorize(req)
        j = req.media
        self.enforce(j,key=str,value=str)
        

    def on_put(self, req, resp, serverId):
        self.authorize(req)
        j = req.media
        self.enforce(j,key=str,value=str)
        self.db.newEnvVar(serverId,j.key,j.value)

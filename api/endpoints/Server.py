import falcon
from db.DB import DB
import re

class Env(object):
    def __init__(self):
        self.db = DB()
        self.supportedAuthorizationTypes = ["token"]

    def enforce(self, j,**kargs):
        for k in kargs.keys():
            if k not in j:
                raise falcon.HTTPMissingParam(k)
            if type(j[k]) != kargs[k]:
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
        resp.media = self.db.getAllEnvVars(serverId)

    def on_put(self, req, resp, serverId):
        self.authorize(req)
        j = req.media
        self.enforce(j,key=str,value=str)
        if not re.match("^\w+(_\w+)*$",j["key"]):
            raise falcon.HTTPInvalidParam("expected key to be 1 word snake case","key")
        self.db.envVar(serverId,j["key"],j["value"])

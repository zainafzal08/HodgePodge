import falcon

class User(object):
    def __init__(self):
        self.supportedAuthorizationTypes = ["token"]
    def authorize(req):
        if "Authorization" not in req.headers:
            raise falcon.HTTPMissingHeader("Authorization")
        components = req.headers["Authorization"].split(" ")
        if len(components) != 2:
            raise falcon.HTTPInvalidHeader("Expected <type> <credentials>", header_name)
        type,creds = components
        if type not in self.supportedAuthorizationTypes:
            raise falcon.HTTPInvalidHeader("Unsupported credential type", header_name)
        
    def on_get(self, req, resp):
        authorize(req)

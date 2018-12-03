import sqlite3

class DB:
    def __init__(self):
        self.url = "db/test.db"
    def execute(self,q,*args):
        conn = sqlite3.connect(self.url)
        c = conn.cursor()
        c.execute(q,tuple(args))
        r = c.fetchall()
        conn.commit()
        conn.close()
        return r
    def authKeys(self):
        l = self.execute("SELECT key from auth_keys")
        return map(lambda x: x[0],l)
    def newUser(self, discordId):
        self.execute("INSERT INTO USERS(DISCORD_ID) VALUES(?)",discordId)
    def getUser(self, discordId):
        r = self.execute("SELECT id,nickname,discord_id,oauth_token FROM USERS WHERE DISCORD_ID=?",discordId)
        r = r[0]
        return {
          "id": r[0],
          "nickname": r[1],
          "discord_id": r[2],
          "oauth_token": r[3]
        }
    def paramaterise(self, obj, *args):
        params = [(k,obj[k]) for k in obj.keys() if k in args]
        query = ",".join(["{}=?".format(x[0]) for x in params])
        values = [x[1] for x in params]
        return (query,values)

    def updateUser(self, discordId, upd):
        if len(self.execute("SELECT * FROM USERS WHERE discord_id=?",discordId)) == 0:
            raise Exception("Unknown User")
        params = self.paramaterise(upd,"nickname","oauth_token")
        if params[0] == "":
            return
        q = "UPDATE USERS SET "
        q += params[0]
        q+= " WHERE discord_id=?"
        params[1].append(discordId)
        self.execute(q,*params[1])

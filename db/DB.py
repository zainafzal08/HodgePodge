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

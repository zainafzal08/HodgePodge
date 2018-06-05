import sqlite3

class Daddy():
    def __init__(self, dbURL):
        self.dbURL = dbURL
        pass

    #TODO: Speed this up / move to real db
    def execute(self, q, *args):
        p = tuple(args)
        conn = sqlite3.connect(self.dbURL)
        c = conn.cursor()
        c.execute(q,p)
        r = c.fetchall()
        conn.commit()
        conn.close()
        return r

    def fetch_user(self, user):
        r = self.execute("SELECT INTERNAL_ID,DISPLAY_NAME FROM USERS WHERE EXTERNAL_ID = ?",user.external_id)
        if len(r) == 0:
            self.execute("INSERT INTO USERS (EXTERNAL_ID) VALUES(?)",user.external_id)
            r = self.execute("SELECT INTERNAL_ID FROM USERS WHERE EXTERNAL_ID=?",user.external_id)
            user.internal_id = r[0]
            user.display_name = None
        else:
            user.internal_id = r[0][0]
            user.display_name = r[0][1]

    def resolve_state(self, state):
        state.validate = True
        self.fetch_user(state.author)
        for i in range(len(state.members)):
            state.members[i] = self.fetch_user(state.members[i])

    def can_trigger(self, module, function, user):
        return True

    def update_display(self, user, name):
        self.execute("UPDATE USERS SET DISPLAY_NAME = ? WHERE INTERNAL_ID = ?",name,user.internal_id)

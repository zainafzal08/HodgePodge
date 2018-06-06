import sqlite3

class User():
    def __init__(self, external_id):
        self.external_id = external_id
        self.display_name = None
        self.internal_id = None
        self.tags = []
        self.permissions = {}

    def has_permission(self, module, function):
        return True

    def get_display(self):
        return self.display_name

    # REMOVE EDVENTUALLY
    def execute(self, dbURL, q, *args):
        p = tuple(args)
        conn = sqlite3.connect(dbURL)
        c = conn.cursor()
        c.execute(q,p)
        r = c.fetchall()
        conn.commit()
        conn.close()
        return r

    def resolve(self, dbURL):
        self.dbURL = dbURL
        r = self.execute(dbURL, "SELECT INTERNAL_ID,DISPLAY_NAME FROM USERS WHERE EXTERNAL_ID = ?",self.external_id)
        if len(r) == 0:
            self.execute(dbURL, "INSERT INTO USERS (EXTERNAL_ID) VALUES(?)",self.external_id)
            r = self.execute(dbURL, "SELECT INTERNAL_ID FROM USERS WHERE EXTERNAL_ID=?",self.external_id)
            self.internal_id = r[0]
            self.display_name = None
        else:
            self.internal_id = r[0][0]
            self.display_name = r[0][1]

    def update_display(self, name):
        self.execute(self.dbURL, "UPDATE USERS SET DISPLAY_NAME = ? WHERE INTERNAL_ID = ?",name,self.internal_id)

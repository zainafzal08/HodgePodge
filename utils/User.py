class User(object):
    def __init__(self, external_entitiy, external_id):
        self.id = None
        self.name = None
        self.resolved = False
        self.tags = set()
        self.admin = False

        self.external_entitiy = external_entitiy
        self.external_id = external_id
        self.external_admin = False
        self.external_tags = set()
        self.external_name = None
        self.conn = None

    def set_db(self, db):
        self.conn = db

    def get_tags(self):
        if not self.resolved:
            self.resolve()
        return self.tags

    def get_id(self):
        if not self.resolved:
            self.resolve()
        return self.id

    def get_display(self):
        if not self.resolved:
            self.resolve()
        if self.name:
            return self.name
        if self.external_name:
            return self.external_name
        return "<No Known Name>"

    def update_display(self, name):
        self.name = name
        self.update()
    # tag stuff
    def add_tag(self, tag):
        if tag.isalnum():
            self.tags.add(tag)
        self.update()
    def remove_tag(self, tag):
        try:
            self.tags.remove(tag)
        except:
            pass
        self.update()

    def is_admin(self):
        if not self.resolved:
            self.resolve()
        return self.admin

    def get_external_tags(self):
        return self.external_tags
    def get_external_name(self):
        return self.external_name
    def get_external_id(self):
        return self.external_id
    def is_external_admin(self):
        return self.external_admin
    def get_external_entitiy(self):
        return self.external_entitiy

    def get_string_tags(self):
        return ",".join([e for e in self.tags if e.isalnum()])

    def create(self):
        conn = self.conn
        c = conn.cursor()
        t = self.get_string_tags()
        c.execute("INSERT INTO USERS(NAME,TAGS,ADMIN) VALUES(NULL,%s,%s) RETURNING ID",(t,False))
        i = c.fetchone()[0]
        e = self.external_entitiy
        ei = self.external_id
        c.execute("INSERT INTO EXTERNAL_USERS(USER_ID,ENTITIY,ID) VALUES(%s,%s,%s)",(i,e,ei))
        conn.commit()
        self.id = i
        self.name = None

    def resolve(self):
        conn = self.conn
        c = conn.cursor()
        e = self.external_entitiy
        i = self.external_id
        c.execute("SELECT USER_ID FROM EXTERNAL_USERS WHERE ENTITIY = %s AND ID = %s",(e,i))
        u = c.fetchone()
        if not u:
            self.create()
        else:
            c.execute("SELECT ID,NAME,TAGS FROM USERS WHERE ID = %s",(u[0],))
            r = c.fetchone()
            self.id = r[0]
            self.name = r[1]
            self.tags = set(r[2].split(","))
        self.resolved = True

    def update(self):
        conn = self.conn
        c = conn.cursor()
        t = self.get_string_tags()
        c.execute("UPDATE USERS SET NAME = %s, TAGS = %s",(self.name,t))
        conn.commit()
    def __eq__(self, other):
        return hash(other) == hash(self)
    def __hash__(self):
        return hash("%s-%s"%(self.get_external_id(),self.get_external_entitiy()))

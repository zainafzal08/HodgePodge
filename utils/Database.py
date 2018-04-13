import psycopg2
import urllib.parse as urlparse
import os

# Create table or entry
# handle entry exists, table exists
# handle table doesn't exist but attempted entry

# jesus this is getting compilcated
# can i just use sql alchemy?
class createRequest():
    def __init__(self, conn, type, table):
        self.conn = conn
        self.table = table
        self.q = None
        self.type = type
        self.validTriggers = {
            "EXISTS": ["NOTHING","DIE","RUN","DUP","CLEAR"],
            "NO_TABLE": ["NOTHING","DIE","RUN","FORCE"],
        }
        self.handle = {
            "EXISTS": self.dieExists(),
            "NO_TABLE": self.dieNoTable()
        }

    def nothing(self):
        pass
    def dieExists(self):
        raise Exception("Request Failed: Entry/Table exists")
    def dieNoTable(self):
        raise Exception("Request Failed: Table does not exist")
    def push(self):
        self.q = self.q%self.filters()
        c = self.conn.cursor()
        c.execute(self.q)
        self.conn.commit()

    # todo
    def forcePushEntry(self):
        pass
    def filters(self):
        pass
    def where(self, filters):
        pass
    def tableExists(self):
        pass
    def entryExists(self):
        pass
    def replace(self):

    # replace entry
    def


    def on(self, trigger, response, *args):
        if trigger not in validTriggers:
            raise Exception("Unknown Trigger '%s'"%trigger)
        if response not in validTriggers[trigger]:
            raise Exception("Unknown Response '%s' for Trigger %s"%(response,trigger))
        # invalid triggers
        if trigger == "EXISTS" and response == "DUP" and self.type == "TABLE":
            raise Exception("Invalid Response: Can Not Create Duplicate Table")
        if trigger == "EXISTS":
            if response == "NOTHING":
                self.handle["EXISTS"] = self.nothing()
            elif response == "RUN":
                self.handle["EXISTS"] = args[0]
            elif response == "DIE":
                self.handle["EXISTS"] = self.dieExists()
            elif response == "DUP":
                self.handle["EXISTS"] = self.push()
            elif response == "REPLACE":
                self.handle["EXISTS"] = self.replace()
            elif response == "CLEAR":
                self.handle["EXISTS"] = self.clear()
            else:
                raise Exception("Internal Error: Attempt to set a unknown response")
        elif trigger == "NO_TABLE":
            if response == "NOTHING":
                self.handle["NO_TABLE"] = self.nothing()
            elif response == "RUN":
                self.handle["NO_TABLE"] = args[0]
            elif response == "DIE":
                self.handle["NO_TABLE"] = self.dieNoTable()
            elif response == "FORCE":
                self.handle["NO_TABLE"] = self.forcePushEntry()
            else:
                raise Exception("Internal Error: Attempt to set a unknown response")
    def execute():
        # check
        tble = self.tableExists()
        if(self.type == "TABLE" and tble):
            self.handle["EXISTS"]()
            return
        elif(self.type == "ENTRY" and not tble):
            self.handle["NO_TABLE"]()
            return
        elif(self.type == "ENTRY" and self.entryExists()):
            self.handle["EXISTS"]()
            return
        # do it
        self.push()

class findRequest():
    def __init__(self, conn):
        self.conn = conn
        self.q = None
    def query(self, q, *args):
        c = self.conn.cursor()
        c.execute(q%args)
        a = c.fetchall()
        return a
    def execute():
        pass

class Db():
    def __init__(self, conn):
        # giving stringised paramaters
        if " " in conn:
            self.conn = psycopg2.connect(conn)
            return
        # giving url
        url = urlparse.urlparse(conn)
        dbname = url.path[1:]
        user = url.username
        password = url.password
        host = url.hostname
        port = url.port
        self.conn = psycopg2.connect(dbname=dbname,user=user,password=password,host=host,port=port)

    def ensure(self,f,l,m):
        for i,e in l:
            if not f(e):
                raise Exception("Element %d of list is invalid, %s"m)

    def create(self, t, n, f):
        t = t.upper()
        q = ""
        if t == "TABLE":
            self.ensure(lambda x: hasattr(x,'__iter__') and len(x) == 2, f, "Must be 2 item itertable object of (fieldName,fieldType)")
            q = "CREATE TABLE %s(%s)"%(n,",".join(["%s %s"%(x[0],x[1]) for x in f]))
            q += "%s"
        elif t == "ENTRY":
            self.ensure(lambda x: type(x) is str, f, "Must be string")
            q = "INSERT INTO TABLE %s VALUES(%s)"%(n,",".join(f))
            q += "%s"
        else:
            raise Exception("%s is a invalid creation type"%t)
        r = createRequest(self.conn,t,n)
        r.q = q
        return r

    def find(self, t, n):
        t = t.upper()
        q = ""
        if t == "ONE":
            q = "SELECT * FROM %s"%n
            q += "%s LIMIT 1
        elif t == "ALL":
            q = "SELECT * FROM %s"%n
            q += "%s"
        else:
            raise Exception("%s is a invalid find type"%t)
        r = findRequest(conn,t,n)
        r.q = q
        return r

class Daddy():
    def __init__(self, db):
        self.db = db

    # flushes the database permissions
    # and users
    #
    def hardFlush(self, **kargs):
        if "imSure" not in kargs:
            raise Exception("ARE YOU SURE")
        if not kargs["imSure"]:
            raise Exception("ARE YOU SURE")
        # do logic

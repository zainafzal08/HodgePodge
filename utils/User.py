class User():
    def __init__(self, external_id):
        self.external_id = external_id
        self.display_name = None
        self.internal_id = None
        self.tags = []
        pass

    def get_display(self):
        return self.display_name

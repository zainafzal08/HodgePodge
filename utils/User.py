from sqlalchemy import Column, ForeignKey, Integer, String, Text, Boolean
from utils.Base import Base

class User(Base):
    __tablename__ = 'users'
    internal_id = Column(Integer, primary_key=True)
    external_id = Column(Text)
    display_name = Column(Text)
    admin = Column(Boolean)

    def set_tags(self, tags):
        for tag in tags:
            try:
                self.add_tag(tag)
            except:
                continue

    def add_tag(self, tag):
        if not hasattr(self,'tags'):
            self.tags = set()
        if not tag.isalnum():
            raise InterfaceException("All tag names must be alpha-numeric")
        self.tags.add(tag)

    def get_tags(self):
        if not hasattr(self,'tags'):
            self.tags = set()
        return self.tags

    def get_display(self):
        return self.display_name

    def __hash__(self):
        return self.internal_id

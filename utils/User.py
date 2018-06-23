from sqlalchemy import Column, ForeignKey, Integer, String, Text, Boolean
from utils.Base import Base

class User(Base):
    __tablename__ = 'users'
    internal_id = Column(Integer, primary_key=True)
    external_id = Column(Text)
    display_name = Column(Text)
    admin = Column(Boolean)
    tags = Column(Text)

    def set_external_name(self, en):
        self.external_name = en

    def set_tags(self, tags):
        for tag in tags:
            try:
                self.add_tag(tag)
            except:
                continue

    def add_tag(self, tag):
        if not tag.isalnum():
            raise InterfaceException("All tag names must be alpha-numeric")
        if(not self.tags):
            self.tags = tag
        else:
            self.tags += ",%s"%tag

    def get_tags(self):
        if not self.tags:
            return None
        return set(self.tags.split(","))

    def get_display(self):
        n = None
        if self.display_name:
            n = self.display_name
        elif hasattr(self,'external_name'):
            n = self.external_name
        if not n:
            return "<No Name Known>"
        return n

    def __hash__(self):
        return self.internal_id

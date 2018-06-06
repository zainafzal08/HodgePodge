from sqlalchemy import Column, ForeignKey, Integer, String, Text
from utils.Base import Base

class User(Base):
    __tablename__ = 'users'
    internal_id = Column(Integer, primary_key=True)
    external_id = Column(Text)
    display_name = Column(Text)

    def has_permission(self, module, function):
        return True

    def get_display(self):
        return self.display_name

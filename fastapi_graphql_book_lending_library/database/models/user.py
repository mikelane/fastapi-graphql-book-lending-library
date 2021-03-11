from sqlalchemy import (
    Column,
    String,
)

from .base import ModelBase


class User(ModelBase):
    email = Column(String(length=255), primary_key=True)

    def __repr__(self):
        return f"<User: {self.email}>"

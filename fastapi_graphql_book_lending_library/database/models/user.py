from graphene_sqlalchemy import SQLAlchemyObjectType
from sqlalchemy import (
    Column,
    String,
)

from .base import ModelBase


class User(ModelBase):
    email = Column(String(length=255), primary_key=True)

    def __repr__(self):
        return f"<User: {self.email}>"


class UserType(SQLAlchemyObjectType):
    class Meta:
        model = User
        only_fields = ["email", "updated_at"]

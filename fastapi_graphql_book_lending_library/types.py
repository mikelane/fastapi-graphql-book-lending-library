from graphene_sqlalchemy import SQLAlchemyObjectType

from fastapi_graphql_book_lending_library.database import models


class User(SQLAlchemyObjectType):
    class Meta:
        model = models.User
        only_fields = ["email", "updated_at"]

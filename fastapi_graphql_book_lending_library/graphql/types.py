from datetime import datetime

from graphene import (
    DateTime,
    Field,
    ObjectType,
    String,
)
from graphene_sqlalchemy import SQLAlchemyObjectType

from fastapi_graphql_book_lending_library.database import models
from fastapi_graphql_book_lending_library.graphql.resolvers import (
    resolve_time,
    resolve_user,
)


class User(SQLAlchemyObjectType):
    class Meta:
        model = models.User
        only_fields = ["email", "updated_at"]
        description = (
            "This is custom graphql User type which is based on a sqlalchemy model"
        )


class ComplexThing(ObjectType):
    """This is a complex object that is not associated with a sqlalchemy
    model. The trick here is to ensure that and sub-resolvers include
    the required parameters (including whether it is a required
    parameter or not).
    """

    user = Field(User, resolver=resolve_user, email=String(required=True))
    time = DateTime(resolver=resolve_time)

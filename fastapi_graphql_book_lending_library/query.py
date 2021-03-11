from datetime import datetime

import graphene
from fastapi_sqlalchemy import db
from loguru import logger

from fastapi_graphql_book_lending_library import types
from fastapi_graphql_book_lending_library.database import models


class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.String(default_value="stranger"))
    time = graphene.DateTime()
    users = graphene.List(types.User)
    user = graphene.Field(types.User, email=graphene.String(required=True))

    def resolve_hello(self, info, name):
        logger.debug(f"Resolving hello {name=!r}")
        return f"Hello, {name}"

    def resolve_time(self, info):
        logger.debug("Returning the UTC datetime")
        return datetime.utcnow()

    def resolve_users(self, info):
        logger.debug(f"Getting all users")
        users = db.session.query(models.User).all()
        return users

    def resolve_user(self, info, email):
        logger.debug(f"Getting user with {email=}")
        user = db.session.query(models.User).get(email)
        return user

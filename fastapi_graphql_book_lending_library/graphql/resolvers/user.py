from fastapi_sqlalchemy import db
from loguru import logger

from fastapi_graphql_book_lending_library.database.models import User


def resolve_users(root, info):
    logger.debug(f"Getting all users")
    users = db.session.query(User).all()
    return users


def resolve_user(root, info, email):
    logger.debug(f"Getting user with {email=}")
    user = db.session.query(User).get(email)
    return user

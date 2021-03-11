__version__ = "0.1.0"

from datetime import datetime

import graphene
import uvicorn
from fastapi import FastAPI
from fastapi_sqlalchemy import (
    DBSessionMiddleware,
    db,
)
from graphene import String
from graphene_sqlalchemy import SQLAlchemyObjectType
from graphene_sqlalchemy.converter import (
    convert_sqlalchemy_type,
    get_column_doc,
    is_column_nullable,
)
from loguru import logger
from sqlalchemy_utils import EmailType
from starlette.graphql import GraphQLApp

from fastapi_graphql_book_lending_library.database.models import User


def create_app() -> FastAPI:
    app = FastAPI(title="CustomLogger", debug=False)
    # logger = CustomizeLogger.make_logger(config_path)
    app.logger = logger

    app.add_middleware(
        DBSessionMiddleware,
        db_url="postgresql://gql_dev_user:password@localhost:25432/book_library",
    )

    return app


app = create_app()


@convert_sqlalchemy_type.register(EmailType)
def convert_column_to_string(type, column, registry=None):
    return String(description=get_column_doc(column))


class UserType(SQLAlchemyObjectType):
    class Meta:
        model = User


class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.String(default_value="stranger"))
    time = graphene.DateTime()
    users = graphene.List(UserType)

    def resolve_hello(self, info, name):
        logger.debug(f"Resolving hello {name=!r}")
        return f"Hello, {name}"

    def resolve_time(self, info):
        return datetime.utcnow()

    def resolve_users(self, info):
        logger.debug(f"{info=}")
        users = db.session.query(User).all()
        return users


app.add_route("/", GraphQLApp(schema=graphene.Schema(query=Query)))

if __name__ == "__main__":
    uvicorn.run("fastapi_graphql_book_lending_library:app", log_level="debug")

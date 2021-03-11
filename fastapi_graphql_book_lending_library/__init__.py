__version__ = "0.1.0"

import graphene
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware
from loguru import logger
from starlette.graphql import GraphQLApp

from fastapi_graphql_book_lending_library.database.models import (
    User,
    UserType,
)

from .query import Query


def create_app() -> FastAPI:
    app = FastAPI(title="CustomLogger", debug=False)
    app.logger = logger

    app.add_middleware(
        DBSessionMiddleware,
        db_url="postgresql://gql_dev_user:password@localhost:25432/book_library",
    )

    return app


app = create_app()

app.add_route("/graphql", GraphQLApp(schema=graphene.Schema(query=Query)))

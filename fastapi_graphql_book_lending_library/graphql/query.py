import graphene
from graphene import String

from fastapi_graphql_book_lending_library.graphql import types
from fastapi_graphql_book_lending_library.graphql.resolvers import (
    resolve_hello,
    resolve_time,
    resolve_user,
    resolve_users,
)
from fastapi_graphql_book_lending_library.graphql.types import ComplexThing


def complex_thing_resolver(
    root,
    info,
):
    return {}


class Query(graphene.ObjectType):
    hello = graphene.String(
        name=graphene.String(default_value="stranger"), resolver=resolve_hello
    )
    time = graphene.DateTime(resolver=resolve_time)
    users = graphene.List(types.User, resolver=resolve_users)
    user = graphene.Field(
        types.User, email=graphene.String(required=True), resolver=resolve_user
    )
    complex_thing = graphene.Field(
        ComplexThing,
        resolver=complex_thing_resolver,
    )

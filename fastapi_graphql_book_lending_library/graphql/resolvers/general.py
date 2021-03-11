from datetime import datetime

from loguru import logger


def resolve_hello(root, info, name):
    logger.debug(f"Resolving hello {name=!r}")
    return f"Hello, {name}"


def resolve_time(root, info):
    logger.debug("Returning the UTC datetime")
    return datetime.utcnow()

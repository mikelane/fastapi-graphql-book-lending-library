from datetime import datetime
from typing import Any

from sqlalchemy import (
    Column,
    DateTime,
)
from sqlalchemy.ext.declarative import (
    as_declarative,
    declared_attr,
)

from .mixins import ModelManagementMixin


@as_declarative()
class Base:
    __name__: str

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


class ModelBase(Base, ModelManagementMixin):
    __abstract__ = True

    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(
        DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow
    )

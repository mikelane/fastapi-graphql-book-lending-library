from fastapi_sqlalchemy import db
from loguru import logger
from sqlalchemy.exc import SQLAlchemyError


class ModelManagementMixin:
    def save(self):
        logger.info(f"Saving {self!r}")
        with db():
            db.session.add(self)
        self._flush()
        return self

    def update(self, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        logger.info(f"Updating {self!r} with {kwargs!r}")
        return self.save()

    def delete(self):
        logger.info(f"Deleting {self!r}")
        with db():
            db.session.delete(self)
        self._flush()

    def _flush(self):
        with db():
            try:
                db.session.flush()
            except SQLAlchemyError as e:
                logger.info(e)
                db.session.rollback()
                raise e

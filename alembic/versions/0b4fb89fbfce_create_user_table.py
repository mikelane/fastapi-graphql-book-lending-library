"""Create User table

Revision ID: 0b4fb89fbfce
Revises: 
Create Date: 2021-03-11 08:36:50.437435+00:00

"""
from datetime import datetime

import sqlalchemy as sa

# revision identifiers, used by Alembic.
from sqlalchemy import (
    DATETIME,
    String,
    func,
)

from alembic import op

revision = "0b4fb89fbfce"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "user",
        sa.Column("email", String(length=255), nullable=False),
        sa.Column(
            "created_at", sa.DateTime(), nullable=False, server_default=func.now()
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(),
            nullable=False,
            server_default=func.now(),
            server_onupdate=func.now(),
        ),
        sa.PrimaryKeyConstraint("email"),
    )


def downgrade():
    op.drop_table("user")

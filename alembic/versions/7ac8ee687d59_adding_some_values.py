"""adding some values

Revision ID: 7ac8ee687d59
Revises: 18cc782f747c
Create Date: 2023-05-19 17:10:26.434396

"""
from alembic import op
import sqlalchemy as sa
from app.models import Post, User
from datetime import datetime


# revision identifiers, used by Alembic.
revision = "7ac8ee687d59"
down_revision = "18cc782f747c"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # User(user_id=1, first_name="John", last_name="Doe")
    # User(user_id=2, first_name="Alice", last_name="Smith")
    # User(user_id=3, first_name="Bob", last_name="Johnson")
    # Post(post_id=1, user_id=1, date=datetime(2023, 5, 17, 10, 30, 0))
    # Post(post_id=2, user_id=2, date=datetime(2023, 5, 16, 15, 45, 0))
    # Post(post_id=3, user_id=3, date=datetime(2023, 5, 15, 20, 0, 0))
    pass


def downgrade() -> None:
    pass

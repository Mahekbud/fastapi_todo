"""add user_id in size in notification

Revision ID: 5f3c8f5ba2c3
Revises: 73bbb405c6af
Create Date: 2024-06-27 18:12:14.962183

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5f3c8f5ba2c3'
down_revision: Union[str, None] = '73bbb405c6af'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###

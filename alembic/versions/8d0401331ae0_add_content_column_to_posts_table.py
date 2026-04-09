"""add content column to posts table

Revision ID: 8d0401331ae0
Revises: 58e38e080d57
Create Date: 2026-04-09 13:47:07.442922

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8d0401331ae0'
down_revision: Union[str, Sequence[str], None] = '58e38e080d57'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass

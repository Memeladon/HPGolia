"""map init

Revision ID: 92e2f5267846
Revises: 5a6eccacaa96
Create Date: 2024-09-09 10:24:01.941536

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '92e2f5267846'
down_revision: Union[str, None] = '5a6eccacaa96'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # TODO: add cells migration
    pass


def downgrade() -> None:
    pass

"""second migration: add column 'address'

Revision ID: dab734291342
Revises: e1204a1005d5
Create Date: 2025-04-10 20:01:23.482888

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "dab734291342"
down_revision: Union[str, None] = "e1204a1005d5"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("Wallets", sa.Column("address", sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("Wallets", "address")
    # ### end Alembic commands ###

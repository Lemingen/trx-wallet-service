"""first migration

Revision ID: e1204a1005d5
Revises:
Create Date: 2025-04-10 18:53:21.260316

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.exc import OperationalError
from sqlalchemy import text, create_engine

from src.config import settings

# revision identifiers, used by Alembic.
revision: str = "e1204a1005d5"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

sync_engine = create_engine(settings.get_sync_db_url)

def create_database_if_not_exists():
    with sync_engine.connect() as connection:
        try:
            result = connection.execute(text("SELECT 1 FROM pg_database WHERE datname='wallet_db'"))
            exists = result.scalar()
            if not exists:
                connection.execute(text("CREATE DATABASE wallet_db"))
                print("Database created.")
            else:
                print("Database already exists.")
        except OperationalError as e:
            print(f"Error checking database: {e}")

def upgrade() -> None:
    create_database_if_not_exists()
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "Wallets",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("bandwidth", sa.Float(), nullable=False),
        sa.Column("energy", sa.Float(), nullable=False),
        sa.Column("balance", sa.Float(), nullable=False),
        sa.Column("date", sa.Date(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("Wallets")
    # ### end Alembic commands ###

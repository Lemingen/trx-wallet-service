import datetime
from src.db import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Date


class WalletRequestOrm(Base):
    __tablename__ = "Wallets"

    id: Mapped[int] = mapped_column(nullable=False, primary_key=True)
    bandwidth: Mapped[float] = mapped_column(nullable=False)
    energy: Mapped[float] = mapped_column(nullable=False)
    balance: Mapped[float] = mapped_column(nullable=False)
    address: Mapped[str] = mapped_column(nullable=False)
    date: Mapped[datetime.date] = mapped_column(Date, nullable=False)

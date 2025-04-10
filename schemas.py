from typing import Optional

from pydantic import BaseModel

from datetime import date


class WalletResponse(BaseModel):
    balance: float
    energy: Optional[int]
    bandwidth: int


class WalletDBResponse(BaseModel):
    id: int
    address: str
    balance: float
    bandwidth: int
    energy: Optional[int]
    date: date

from fastapi import FastAPI
from src.service import get_wallet_params
from src.db import async_session_factory
from src.models import WalletRequestOrm
from datetime import date
from src.schemas import WalletResponse, WalletDBResponse
from typing import List
from sqlalchemy.future import select

app = FastAPI()


@app.post(
    "/create_wallet_info/",
    response_model=WalletResponse,
    summary="Save wallet info to the database",
    description="Получает информацию о кошельке Tron по адресу, сохраняет её в базу данных и возвращает данные",
    response_description="Информация о кошельке: balance, energy, bandwidth",
)
async def create_wallet_info(address: str) -> dict:
    balance, energy, bandwidth = get_wallet_params(address)
    data = WalletRequestOrm(
        bandwidth=bandwidth,
        energy=energy,
        balance=balance,
        address=address,
        date=date.today(),
    )
    async with async_session_factory() as session:
        async with session.begin():
            session.add(data)
            await session.commit()  # type: ignore

    return {"bandwidth": bandwidth, "energy": energy, "balance": balance}


@app.get(
    "/get_wallet_info/",
    response_model=List[WalletDBResponse],
    summary="Get wallet info from the database",
    description="Возвращает сохранённые записи о кошельках Tron из базы данных с поддержкой пагинации",
    response_description="Список записей с информацией о кошельках Tron",
)
async def get_wallet_info(offset: int, limit: int) -> List[dict]:
    async with async_session_factory() as session:
        async with session.begin():
            result = await session.execute(
                select(WalletRequestOrm).offset(offset).limit(limit)
            )
            records = result.scalars().all()
            return [
                {
                    "id": r.id,
                    "address": r.address,
                    "balance": r.balance,
                    "bandwidth": r.bandwidth,
                    "energy": r.energy,
                    "date": r.date.isoformat(),
                }
                for r in records
            ]

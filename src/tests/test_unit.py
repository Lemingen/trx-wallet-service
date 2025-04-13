import pytest
from datetime import date
from src.db import async_session_factory
from src.models import WalletRequestOrm
from sqlalchemy import select


@pytest.fixture
def sample_wallet():
    return {
        "address": "TXYZ1234567890",
        "balance": 100.5,
        "bandwidth": 500.0,
        "energy": 300.0,
        "date": date.today(),
    }


@pytest.mark.asyncio  # Добавляем декоратор для асинхронных тестов
async def test_create_wallet_record(sample_wallet):
    data = WalletRequestOrm(**sample_wallet)

    # Операции с базой данных должны быть асинхронными
    async with async_session_factory() as session:
        async with session.begin():
            session.add(data)
            await session.commit()  # Используем await для асинхронных операций
            wallet_id = data.id

    # Проверка, что данные записались в БД
    async with async_session_factory() as session:
        async with session.begin():
            result = await session.execute(
                select(WalletRequestOrm).filter_by(id=wallet_id)
            )
            result = result.scalar_one_or_none()

            assert result is not None
            assert result.address == sample_wallet["address"]
            assert result.balance == sample_wallet["balance"]

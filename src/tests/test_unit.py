import pytest
from datetime import date
from src.db import async_session_factory
from src.models import WalletRequestOrm


@pytest.fixture
def sample_wallet():
    return {
        "address": "TXYZ1234567890",
        "balance": 100.5,
        "bandwidth": 500.0,
        "energy": 300.0,
        "date": date.today(),
    }


def test_create_wallet_record(sample_wallet):
    data = WalletRequestOrm(**sample_wallet)

    async with async_session_factory() as session:
        async with session.begin():
            session.add(data)
            session.commit()
            wallet_id = data.id

    async with async_session_factory() as session:
        async with session.begin():
            result = session.query(WalletRequestOrm).filter_by(id=wallet_id).first()

            assert result is not None
            assert result.address == sample_wallet["address"]
            assert result.balance == sample_wallet["balance"]

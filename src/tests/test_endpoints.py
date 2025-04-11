from fastapi.testclient import TestClient
from src.api import app

client = TestClient(app)


def test_post_and_get_wallet_info():
    address = "TWwXD1fgvBsaSkF7qktTrysCCL98fu5tf3"

    response = client.post("/create_wallet_info/", params={"address": address})
    assert response.status_code == 200
    data = response.json()
    assert "bandwidth" in data
    assert "energy" in data
    assert "balance" in data

    response = client.get("/get_wallet_info/?offset=0&limit=5")
    assert response.status_code == 200
    records = response.json()
    assert isinstance(records, list)
    assert any(r["address"] == address for r in records)

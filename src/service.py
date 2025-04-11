from tronpy import Tron  # type: ignore
from tronpy.providers import HTTPProvider  # type: ignore
from src.config import settings


def get_wallet_params(addr: str) -> tuple[float, float, float]:
    tron = Tron(provider=HTTPProvider(api_key=settings.get_api_key))
    account = tron.get_account(addr)
    balance = account["balance"] / 1e6
    resource = account.get("account_resource", {})
    used_energy = resource.get("energy_usage")
    if used_energy is None:
        used_energy = 0

    bandwidth = tron.get_bandwidth(addr)
    return (balance, used_energy, bandwidth)

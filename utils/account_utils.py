from dataclasses import dataclass
from typing import *

from utils.coinbase_api_utils import get_coinbase_client


@dataclass
class CoinAccount:
    """
    Utility class for Coinbase accounts
    """
    def __init__(
        self,
        coinbase_account: dict
    ) -> None:
        self.name = coinbase_account.name
        self.balance_amount = float(coinbase_account.balance.amount)
        self.balance_currency = coinbase_account.balance.currency
        self.native_balance_amount = float(coinbase_account.native_balance.amount)
        self.native_balance_currency = coinbase_account.native_balance.currency

    @property
    def is_active(self):
        return bool(self.balance_amount)

    @property
    def account_balance(self):
        return f"{self.balance_amount} {self.balance_currency}"
    
    @property
    def account_native_balance(self):
        return f"{self.native_balance_amount} {self.native_balance_currency}"

    @property
    def summary_info(self) -> str:
        return f"{self.name} - {self.account_balance} - {self.account_native_balance}"
    
    def __repr__(self) -> str:
        return self.summary_info

    def __str__(self) -> str:
        return self.summary_info


def fetch_accounts(
    return_active: bool = True
) -> List[CoinAccount]:

    client = get_coinbase_client()
    all_accounts = client.get_accounts().data
    accounts_to_return = []
    for account in all_accounts:
        coin_account = CoinAccount(account)
        if return_active and coin_account.is_active is False:
            continue
        accounts_to_return.append(coin_account)
    
    return accounts_to_return
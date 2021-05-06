import os
from typing import *
from dataclasses import dataclass

from coinbase.wallet.client import Client
from dotenv import load_dotenv

@dataclass
class CoinAccount:
    name: str
    balance_amount: float
    balance_currency: str
    native_balance_amount: float
    native_balance_currency: str

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
        
load_dotenv()
COINBASE_API_KEY = os.environ.get("COINBASE_API_KEY")
COINBASE_API_SECRET = os.environ.get("COINBASE_API_SECRET")

client = Client(COINBASE_API_KEY, COINBASE_API_SECRET)


for account in client.get_accounts().data:
    coin_account = CoinAccount(
        account.name,
        float(account.balance.amount),
        account.balance.currency,
        float(account.native_balance.amount),
        account.native_balance.currency,
    )

    if coin_account.is_active:
        print(coin_account.summary_info)






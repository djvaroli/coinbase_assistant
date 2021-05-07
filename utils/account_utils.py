from dataclasses import dataclass
from typing import *

from coinbase.wallet.model import Account
from utils.coinbase_api_utils import get_coinbase_client


class ExtendedCoinbaseAccount(object):
    def __init__(
        self,
        account: Account
    ):
        self.account = account

    def __getattr__(self, attr):
        print(attr)
        return getattr(self.account, attr)

    def __repr__(self) -> str:
        return self.account.__repr__()
    
    def __str__(self) -> str:
        return self.account.__str__()

    @property
    def is_active(self):
        account_balance = self.account.balance.amount
        return bool(account_balance)

    @property
    def summary_info(self) -> str:
        name = self.name
        balance_amount = self.balance.amount
        balance_currency = self.balance.currency
        native_balance_amount = self.native_balance.amount
        native_balance_currency = self.native_balance.currency

        return f"{name} - {balance_amount} {balance_currency} - {native_balance_amount} {native_balance_currency}"

    
def fetch_accounts(
    return_active: bool = True
) -> List[ExtendedCoinbaseAccount]:

    client = get_coinbase_client()
    accounts = client.get_accounts().data
    accounts_to_return = []
    for account in accounts:
        account = ExtendedCoinbaseAccount(account)
        if return_active and account.is_active is False:
            continue
        accounts_to_return.append(account)
    return accounts_to_return


def get_account_net_input_amount(
    account_id: str = None,
    account: Optional[Account] = None
):
    """
    returns USD amount equalling cumulative amount of money
    put into account
    """
    assert account_id or account, "Must provide either account_id or instance of Account"

    if account_id and not account:
        client = get_coinbase_client()
        account_transactions = client.get_transactions(account_id)
    else:
        account_transactions = account.get_transactions()
    
    account_net_buy = 0
    for transaction in account_transactions.data:
        transaction_type = transaction.type
        if transaction_type != "buy":
            continue
        purchase_amount_usd = float(transaction.native_amount.amount)
        account_net_buy += purchase_amount_usd
    
    return account_net_buy
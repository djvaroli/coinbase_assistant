import os
from typing import *
from utils.account_utils import fetch_accounts, ExtendedCoinbaseAccount
from utils.messaging_utils import send_sms

if __name__ == "__main__":
    accounts: List[ExtendedCoinbaseAccount] = fetch_accounts()
    account_summaries = "\n".join([a.summary_info for a in accounts])
    send_sms(body=account_summaries)






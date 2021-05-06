import os
from typing import *
from utils.account_utils import fetch_accounts
from utils.messaging_utils import send_sms

if __name__ == "__main__":
    accounts = fetch_accounts()
    accounts = [str(account) for account in accounts]
    sms_friendly_accounts = "\n".join(accounts)
    send_sms(to="+18579996528", body=sms_friendly_accounts)






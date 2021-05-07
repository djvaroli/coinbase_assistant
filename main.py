import os
from typing import *
from utils.portfolio_utils import Portfolio
from utils.messaging_utils import send_sms

if __name__ == "__main__":
    portfolio = Portfolio()
    portfolio_breakdown = portfolio.breakdown(format_for_sms=True)

    send_sms(body=portfolio_breakdown)






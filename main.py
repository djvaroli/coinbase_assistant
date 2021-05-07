import os
from typing import *
from utils.portfolio_utils import Portfolio
from utils.messaging_utils import send_sms

if __name__ == "__main__":
    portfolio = Portfolio()
    portfolio_breakdown = portfolio.breakdown()
    
    message = f"Portfolio Net Value: {portfolio_breakdown}"
    send_sms(body=account_summaries)






import os
from typing import *

from fastapi import FastAPI

from app.utils.portfolio_utils import Portfolio
from app.utils.messaging_utils import send_sms


app = FastAPI()



app.get("/portfolio")
if __name__ == "__main__":
    portfolio = Portfolio()
    portfolio_breakdown = portfolio.breakdown(format_for_sms=True)

    send_sms(body=portfolio_breakdown)






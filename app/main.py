import os
from typing import *

from fastapi import FastAPI

from app.utils.portfolio_utils import Portfolio
from app.utils.messaging_utils import send_sms


app = FastAPI()


@app.get("/")
def home():
    return "Welcome!"


@app.get("/portfolio")
def get_portfolio():
    portfolio = Portfolio()
    
    return portfolio.breakdown()


@app.get("/portfolio/sms_update")
def send_portfolio_sms_update():
    portfolio_summary = Portfolio().breakdown(format_for_sms=True)
    message_id = send_sms(body=portfolio_summary)
    return message_id

    





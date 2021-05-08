import os
from typing import *

from fastapi import FastAPI

from app.routers import portfolio
from utils.portfolio_utils import Portfolio
from utils.messaging_utils import send_sms


app = FastAPI()

app.include_router(portfolio.router)

@app.get("/")
def home():
    return "Welcome!"




    





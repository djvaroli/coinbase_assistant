import os
from typing import *

from fastapi import FastAPI

from app.routers import portfolio


app = FastAPI()
app.include_router(portfolio.router)


@app.get("/")
def home():
    return "Welcome!"




    





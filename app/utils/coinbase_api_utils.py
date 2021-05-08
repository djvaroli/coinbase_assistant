import os

from coinbase.wallet.client import Client
from dotenv import load_dotenv


load_dotenv()
COINBASE_API_KEY = os.environ.get("COINBASE_API_KEY")
COINBASE_API_SECRET = os.environ.get("COINBASE_API_SECRET")


def get_coinbase_client():
    return Client(COINBASE_API_KEY, COINBASE_API_SECRET)


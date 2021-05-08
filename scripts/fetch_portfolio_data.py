import os
import logging
import simplejson as json
from datetime import datetime as dt
from pathlib import Path
from utils import portfolio_utils

ROOT_DIR = os.path.dirname(os.path.abspath(__name__))
DATA_DIR = Path(os.path.join(ROOT_DIR, "historical_data"))


def main():
    portfolio = portfolio_utils.Portfolio()
    new_data = portfolio.breakdown()
    date_key = dt.now().strftime("%B-%d-%Y")
    filepath = DATA_DIR / f"{date_key}.json"

    data = []
    if filepath.exists():
        with open(filepath, "r") as f:
            data = json.load(f)
        data.append(new_data)
    else:
        data = [new_data]
    
    with open(filepath, "w+") as f:
        json.dump(data, f)


if __name__ == "__main__":
    main()


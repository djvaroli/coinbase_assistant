import os
import requests
import simplejson as json
from datetime import datetime as dt
from pathlib import Path


ROOT_DIR = os.path.dirname(os.path.abspath(__name__))
DATA_DIR = Path(os.path.join(ROOT_DIR, "historical_data"))
if not DATA_DIR.exists(DATA_DIR):
    DATA_DIR.mkdir()


def main():
    url = "http://localhost/portfolio/"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Request failed with status code {response.status_code}.")

    date = dt.now().isoformat()
    date_key = dt.now().strftime("%B-%d-%Y")
    new_data = response.json()
    new_data['date'] = date

    filepath = DATA_DIR / f"{date_key}.json"

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


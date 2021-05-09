cd ~/Desktop/coding/cryptos/coinbase || exit
python3 -m pip install --upgrade pip
python3 -m pip install -r calypso/requirements.txt
python3 -m pip install custom/
python3 scripts/fetch_portfolio_data.py
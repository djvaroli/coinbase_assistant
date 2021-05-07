# Simple Assitant for Coinbase Crypto-currency Wallet

The motivation for building this was the desire to view quick summary info regarding my Crypto-currency portfolio on Coinbase. I wanted to know how much money I put in and how much my portfolio was worth in addition to what accounts contributed how much. I was not able to find an easy way to do so with Coinbase directly, however fortunately they have a nice API.

## Running Locally

To run this for yourself you will need to clone the repo by opening a starting up a shell and running
`git clone https://github.com/djvaroli/coinbase_assistant.git coinbase_assistant/ && cd coinbase_assistant`

You can then create a virtual python environment and install all the required dependencies
```
python -m venv venv/
source venv/bin/activate
pip install -r requirements.txt
```

Once that is done you will need to create a `.env` file where you will add your twilio and coinabse API keys. It should look something like this
```
COINBASE_API_KEY=<YOUR_COINBASE_API_KEY>
COINBASE_API_SECRET=<YOUR_COINBASE_API_SECRET>
TWILIO_ACCOUNT_SID=<YOUR_TWILIO_ACCOUNT_SID>
TWILIO_AUTH_TOKEN=<YOUR_TWILIO_AUTH_TOKEN>
TWILIO_PHONE_NUMBER=<YOUR_TWILIO_PHONE_NUMBER>
DEFAULT_TO_PHONE_NUMBER=<YOUR_DEFAULT_TO_PHONE_NUMBER> 
```

The phone numbers are set just so that twilio has some default values for sending text messages.

Finally you can simply run `python main.py` and you should get an update with the easy-to-view portfolio summaries.


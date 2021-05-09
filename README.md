# Simple Assitant for Coinbase Crypto-currency Wallet

The motivation for building this was the desire to view quick summary info regarding my Crypto-currency portfolio on Coinbase. I wanted to know how much money I put in and how much my portfolio was worth in addition to what accounts contributed how much. I was not able to find an easy way to do so with Coinbase directly, however fortunately they have a nice API.

## Running Locally

To run this for yourself you will need to clone the repo by opening a starting up a shell and running
`git clone https://github.com/djvaroli/coinbase_assistant.git coinbase_assistant/ && cd coinbase_assistant`

You can then create a virtual python environment and install all the required dependencies
```
python -m venv venv/
source venv/bin/activate
pip install --upgrade pip
pip install -e custom/
pip install -r calypso/requirements.txt
```

Once that is done you will need to create a `.env` file where you can add your twilio and coinabse API keys. You also need to specify the version for docker-compose, but that can be set to anything. 
It should look something like this
```
COINBASE_API_KEY=<YOUR_COINBASE_API_KEY>
COINBASE_API_SECRET=<YOUR_COINBASE_API_SECRET>
TWILIO_ACCOUNT_SID=<YOUR_TWILIO_ACCOUNT_SID>
TWILIO_AUTH_TOKEN=<YOUR_TWILIO_AUTH_TOKEN>
TWILIO_PHONE_NUMBER=<YOUR_TWILIO_PHONE_NUMBER>
DEFAULT_TO_PHONE_NUMBER=<YOUR_DEFAULT_TO_PHONE_NUMBER>
VERSION=1.0 
```

The phone numbers are set just so that twilio has some default values for sending text messages.

## Running with Docker
If you have Docker installed, to startup the server simply run 
```
# from inside the root directory
docker-compose up
```
This will make the backend component of the assistant available at `http://localhost:80`.


## Running with uvicorn directly
If you do not have Docker installed, or you want to run the service in debug mode simply run
```
uvicorn calypso.app.main:app --reload
```
If you do not want hot-reloading to be enabled simply drop the `--reload` flag.


## Setting up crontab job

Currently I have a set up that fetches the portfolio breakdown every 5 minutes. This job is set up using crontab. If you would like to enable that, there is a script that will handle it for you.
Simply run
```
bash scripts/set_up_cron_job.sh
```

## Future 

Currently, I am planning to add a front-end interface with some added features, intuitive visualizations and most likely some simple machine learning to try and forcast how things will go. I am also planning to Dockerise all of it so that running this locally would be as simple as a couple of docker commands. Stay tuned for the updates!


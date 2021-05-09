
# check that the service is running
response=$(curl --write-out "%{http_code}" --silent --output /dev/null "localhost:80")

if [ "$response" != "200" ]; then
    echo "Could not reach Calypso service. Make sure it's running."
    exit 1;
fi

# create a directory for logs
mkdir logs/

#write out current crontab
crontab -l > calypso_cron

#echo new cron into cron file
# if you want to change the frequence change the leading pattern
echo "*/5 * * * * cd ~/Desktop/coding/cryptos/coinbase && bash scripts/fetch_portfolio_data.sh >>logs/stdout.log 2>>logs/stderr.log" >> calypso_cron

#install new cron file
crontab calypso_cron
rm calypso_cron
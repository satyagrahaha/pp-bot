# pp-bot
Discord bot for PP &amp; Friends server.

## Installation
pp-bot is designed to run on EC2 instances. 

1. Clone the project into /home/ubuntu. 
2. Configure with your token (as below). 
3. `cp pp-bot.service /lib/systemd/system/`
4. `sudo systemctl enable pp-bot.service`
5. `sudo systemctl start pp-bot.service`

## Configuration
pp-bot takes its credentials from pp-bot/config.

*example:*
```
[DEFAULT]
token=XXXXXXXXXXXXXXXXXXXX

[TESTING]
token=XXXXXXXXXXXXXXXXXXXX
log=/var/log/pp-bot.testing.log
```

## Profiles
pp-bot will use the DEFAULT configuration when started with no arguments, but an alternate profile can be passed when starting.

*example:*
`python3 main.py TESTING`

## Responses
pp-bot will respond with phrases from pp-bot/response.

## Logging
pp-bot logs to /var/log/pp-bot.log by default or the file specified in config.

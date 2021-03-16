import random
import configparser
import sys
import logging

#local files
import ppbot

#populate responses
responses = open("responses").readlines()

#create client
client = ppbot.ppbot()

#read config file
config = configparser.ConfigParser()
config.read('config')

#read args
if len(sys.argv) > 1:
    if sys.argv[1] == 'help':
        sys.exit("Usage: python3 main.py [PROFILE_NAME]")
    else:
        profile = sys.argv[1]
else:
  profile = 'DEFAULT'

#get token
token = config[profile]['token']

#setup log
if config.has_option(profile,'log'):
  log = config[profile]['log']
else:
  log = "/var/log/pp-bot.log"
logging.basicConfig(filename=log,level=logging.DEBUG,format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

#start client
client.run(token)

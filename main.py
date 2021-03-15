import discord
import random
import configparser
import sys
import logging

class PP_BOT(discord.Client):

  async def on_ready(self):
    logging.info('Logged on as {0}!'.format(self.user))
    
  async def on_message(self, message):
    try:
      if self.user.id in message.raw_mentions:
        await message.channel.send(random.choice(responses))        
    except HTTPException:
      logging.error('Message Send: HTTP Exception!')
    except Forbidden:
      logging.error('Message Send: Forbidden!')
    except InvalidArgument:
      logging.error('Message Send: InvalidArgument!')
      
  async def on_raw_reaction_add(self, payload):

    if payload.emoji.name == 'shame':
      channel = await self.fetch_channel(payload.channel_id)
      message = await channel.fetch_message(payload.message_id)
      await message.add_reaction('<:shame:818856957364535297>')

#populate responses
responses = open("responses").readlines()

#create client
client = PP_BOT()

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


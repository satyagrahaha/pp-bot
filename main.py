import discord
import random
import configparser

class PP_BOT(discord.Client):

  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))
    
  async def on_message(self, message):
    try:
      if self.user.id in message.raw_mentions:
        await message.channel.send(random.choice(responses))        
    except HTTPException:
      print('HTTP Exception!')
    except Forbidden:
      print('Forbidden!')
    except InvalidArgument:
      print('InvalidArgument!')
      
  async def on_raw_reaction_add(self, payload):

    if payload.emoji.name == 'shame':
      channel = await self.fetch_channel(payload.channel_id)
      message = await channel.fetch_message(payload.message_id)
      await message.add_reaction('<:shame:818856957364535297>')
  
client = PP_BOT()

config = configparser.ConfigParser()
config.read('config')

responses = ['I\'m sorry. Did someone say my name?', \
             'With friends like these, who needs friends?', \
             '#becool', 'Y\'all like Shrek?', '..' ]

token = config['DEFAULT']['token']

client.run(token)

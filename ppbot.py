import discord
import logging

class ppbot(discord.Client):

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

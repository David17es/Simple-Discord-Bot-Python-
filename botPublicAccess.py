# This is a simple Discord bot that responds to messages and can fetch memes.
# Make sure to install the required libraries using 'pip install discord requests' in your terminal.

import discord, requests, json

def get_meme():
  response = requests.get('https://meme-api.com/gimme')
  json_data = json.loads(response.text)
  return json_data['url']

class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))

  async def on_message(self, message):
    if message.author == self.user:
      return
    
    if message.content.startswith('$meme'):
      await message.channel.send(get_meme())
    elif message.content.startswith('$hello'):
      await message.channel.send('Hello! I am your friendly Discord bot. How can I assist you today?')
    elif message.content.startswith('$help'):
      help_message = (
          "Here are the commands you can use:\n"
          "`$meme` - Get a random meme.\n"
          "`$hello` - Greet the bot.\n"
          "`$help` - Show this help message."
      )
      await message.channel.send(help_message)


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('Add your token here!') #Replace the token with your own bot token from the Discord Developer Portal.
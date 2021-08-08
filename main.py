import json
from discord.ext import commands
from jishaku import Jishaku

with open('config.json') as json_config:
    config = json.load(json_config)


client = commands.Bot(command_prefix='m!')
client.load_extension('jishaku')

client.load_extension('Cog.Utility')
client.load_extension('Cog.Status')

green = 0x11ff00
red = 0xff0000
yellow = 0xfff200
blue = 0x0055ff

@client.event
async def on_ready():
    print("Ready to destroy the X!")


client.run(config["token"])
import json
import asyncio
import discord
from discord.ext import commands
from jishaku import Jishaku

with open('config.json') as json_config:
    config = json.load(json_config)

client = commands.Bot(command_prefix='m!')
client.load_extension('jishaku')

client.load_extension('Cog.Utility')
client.load_extension('Cog.Status')
client.load_extension('Cog.Moderation')

green = 0x11ff00
red = 0xff0000
yellow = 0xfff200
blue = 0x0055ff

@client.event
async def on_ready():
    print("Ready to destroy the X!")
    client.loop.create_task(status_task())

async def status_task():
    while True:
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="X die"))
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="m!help"))
        await asyncio.sleep(10)

client.run(config["token"])
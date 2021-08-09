import json
import discord
from discord.ext import commands

green = 0x11ff00
red = 0xff0000
yellow = 0xfff200
blue = 0x0055ff

class Settings(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def prefix(self, ctx):
        await ctx.send("Custom prefixes are coming soon")

def setup(client):
    client.add_cog(Settings(client))
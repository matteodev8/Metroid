from os import name
import discord
from discord.ext import commands

green = 0x11ff00
red = 0xff0000
yellow = 0xfff200
blue = 0x0055ff

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client


def setup(client):
    client.add_cog(Moderation(client))
        
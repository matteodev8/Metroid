from os import name
import discord
from discord.ext import commands

green = 0x11ff00
red = 0xff0000
yellow = 0xfff200
blue = 0x0055ff

class Moderation(commands.Cog): # WORK IN PROGRESS
    def __init__(self, client):
        self.client = client       

    @commands.command
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        channel = discord.Embed(title=f"{member.name} has been banned by {ctx.author.name}", description=f"Reason: {reason}", color=red) #This will send the message to the channel
        user = discord.Embed(title=f"You have been banned by {ctx.author.name} in {ctx.guild.name}", desc)

        



#def setup(client):
#    client.add_cog(Moderation(client))       
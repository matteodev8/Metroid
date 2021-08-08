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

    @commands.command
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        channel = discord.Embed(title=f"{member.name} has been banned by {ctx.author.name}", description=f"Reason: {reason}", color=red) 
        user = discord.Embed(title=f"You have been banned by {ctx.author.name} in {ctx.guild.name}", description=f"Reason: {reason}", color=red) 
        try:
            await member.send(embed=user)
        except:
            await ctx.send("I couldn't DM the user. I will still continue to ban.")
        await ctx.send(embed=channel)
        await member.ban(reason = reason) 

    @commands.comamnd
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        channel = discord.Embed(title=f"{member.name} has been kicked by {ctx.author.name}", description=f"Reason: {reason}", color=red) 
        user = discord.Embed(title=f"You have been kicked by {ctx.author.name} in {ctx.guild.name}", description=f"Reason: {reason}", color=red) 
        try:
            await member.send(embed=user)
        except:
            await ctx.send("I couldn't DM the user. I will still continue to kick") 
        await ctx.send(embed=channel)
        await member.kick(reason = reason)

def setup(client):
    client.add_cog(Moderation(client))       
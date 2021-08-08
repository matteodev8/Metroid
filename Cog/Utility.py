import discord
from discord.ext import commands

green = 0x11ff00
red = 0xff0000
yellow = 0xfff200
blue = 0x0055ff

class Utility(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        latency = int(round(self.client.latency * 1000))
    
        if latency < 150:
           pingEmbed=discord.Embed(
               title="Pong! :ping_pong:",
               description=f"{latency}ms (Stable)",
               color=green
           )
        elif latency >= 150:
            pingEmbed=discord.Embed(
                title="Pong! :ping_pong:",
                description=f"{latency}ms (Unstable)",
                color=yellow
            )
        elif latency >= 300:
            pingEmbed=discord.Embed(
                title="Pong! :ping_pong:",
                description=f"{latency}ms (Critical)",
                color=red
            )
        
        await ctx.send(embed=pingEmbed)

def setup(client):
    client.add_cog(Utility(client))
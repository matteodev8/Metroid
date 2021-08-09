import discord
from discord.ext import commands
import statcord

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

    @commands.command()
    async def invite(self, ctx):
        inviteEmbed=discord.Embed(
            title="Invite the bot",
            description="You can invite the bot [here](https://discord.com/api/oauth2/authorize?client_id=872091516837953546&permissions=8&scope=bot)",
            color=blue
        )

        await ctx.send(embed=inviteEmbed)

    @commands.command()
    async def debug(self, ctx):
        debugEmbed=discord.Embed(
            title="mDebug",
            description="Debugger by matteodev",
            color=blue,
        )
        debugEmbed.add_field(name="Executed by", value=f"Command has been executed by {ctx.author.id}")
        debugEmbed.footer("Version 1a")
        
        await ctx.send(embed=debugEmbed)

def setup(client):
    client.add_cog(Utility(client))
import discord
from discord.ext import commands
import statcord
import requests
import aiohttp
import os

green = 0x11ff00
red = 0xff0000
yellow = 0xfff200
blue = 0x0055ff

class Stats(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.key = "statcord.com-BN3cdo3zfi0S04woDCWM"
        self.api = statcord.Client(self.client,self.key)
        self.api.start_loop()

    @commands.Cog.listener()
    async def on_command(self, ctx):
        self.api.command_run(ctx)

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def stats(self, ctx):
      async with aiohttp.ClientSession():
        response = requests.get('https://api.statcord.com/v3/851064798333501480')
        data = response.json()
        pdata = data['data']
        for d in pdata:
            usercount = (d['users'])
            cpu = (d['cpuload'])
            memload = (d['memload'])
        python = "3.9.6"
        discordpy = "1.7.6"
        latency=f"{round(self.client.latency * 1000)}ms"

        embed=discord.Embed(title="Metroid Stats",color=red)
        embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/872091516837953546/7412c4348a367b75b3ac63d842c30822.webp?size=256')        
        embed.add_field(name="Server Count :family_mmbb:",value=len(self.client.guilds))
        embed.add_field(name="User Count :bust_in_silhouette:",value=f"{usercount}")
        embed.add_field(name="CPU Load <:CPU:870908659897610250>",value=f"{cpu}%")
        embed.add_field(name="MEM Load <:RAM:870907903513612299>",value=f"{memload}MB")
        embed.add_field(name="Python <:Python:860913381850480650>", value=python)
        embed.add_field(name="Discord.py <:Discord:860913504361644032>", value=discordpy)
        embed.add_field(name="Latency :ping_pong:", value=latency)
        embed.add_field(name="Operating System <:Darwin:874005917794979920>", value="Darwin")
        embed.set_footer(icon_url='https://cdn.statcord.com/logo.png',text=f"Powered by Statcord")
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Stats(client))
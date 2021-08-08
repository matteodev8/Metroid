import discord
from discord.ext import commands

green = 0x11ff00
red = 0xff0000
yellow = 0xfff200
blue = 0x0055ff

class Status(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingPermissions):
            missingPermissionEmbed=discord.Embed(
                title="Error ❌",
                description="There was an error while executing this command: ```\nUSER_MISSING_PERMISSION\n```",
                color=red
            )
            await ctx.send(embed=missingPermissionEmbed)
            await ctx.message.add_reaction("❌")

        elif isinstance(error, commands.errors.BotMissingPermissions):
            botMissingPermissionEmbed=discord.Embed(
                title="Error ❌",
                description="There was an error while executing this command: ```\nBOT_MISSING_PERMISSION\n```",
                color=red
            )
            await ctx.send(embed=botMissingPermissionEmbed)
            await ctx.message.add_reaction("❌")

        elif isinstance(error, commands.errors.MissingRequiredArgument):
            missingArgumentEmbed=discord.Embed(
                title="Error ❌",
                description="There was an error while executing this command: ```\nMISSING_ARGUMENT\n```",
                color=red
            )
            await ctx.send(embed=missingArgumentEmbed)
            await ctx.message.add_reaction("❌")

        elif isinstance(error, commands.errors.BadArgument):
            badArgumentEmbed=discord.Embed(
                title="Error ❌",
                description="There was an error while executing this command: ```\nBAD_ARGUMENT\n```",
                color=red
            )
            await ctx.send(embed=badArgumentEmbed)
            await ctx.message.add_reaction("❌")

        elif isinstance(error, commands.errors.CommandNotFound):
            missingArgumentEmbed=discord.Embed(
                title="Error ❌",
                description="There was an error while executing this command: ```\nCOMMAND_NOT_FOUND\n```",
                color=red
            )
            await ctx.send(embed=missingArgumentEmbed)
            await ctx.message.add_reaction("❌")

        elif isinstance(error, commands.errors.CommandInvokeError):
            commandInvokeEmbed=discord.Embed(
                title="Critical ⛔️",
                description="There was an critical error while executing this command! The developers have been notified about this issue!",
                color=red
            )
            await ctx.send(embed=commandInvokeEmbed)
            await ctx.message.add_reaction("⛔️")

def setup(client):
    client.add_cog(Status(client))
    

        
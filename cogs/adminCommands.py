import os
import json
import discord
import utils.utils as ut
from discord.ext import tasks, commands
# from dotenv import load_dotenv


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # we unload the bot command
    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx, cog: str):
        try:
            self.bot.unload_extension(cog)
        except Exception as errors:
            await ctx.send(f"the extnension didn't get unloaded")
            return
        await ctx.send(f"the extnension got unloaded")

    # we load the bot command
    @commands.command()
    @commands.is_owner()
    async def load(self, ctx, cog: str):
        try:
            self.bot.load_extension(cog)
        except Exception as errors:
            await ctx.send(f"the extnension didn't get loaded")
            return
        await ctx.send(f"the extnension got loaded")

    # we reload the bot command
    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx, cog: str):
        try:
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
        except Exception as errors:
            await ctx.send(f"the extnension didn't get reloaded")
            return
        await ctx.send(f"the extnension got reloaded")


def setup(bot):
    bot.add_cog(Admin(bot))

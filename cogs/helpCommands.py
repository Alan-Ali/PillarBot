import os
import json
import discord
import utils.utils as ut
from discord.ext import tasks, commands
from dotenv import load_dotenv



class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(pass_context=True)
    async def help(self, ctx):
        # if string == "":
        embed = discord.Embed(
            description=f"**help** use this command to get information about the commands\n**pillar** use this command to get the pillars and prefixes\n**prefix** use this command with a string after to change prefix like this ```%prefix *```(only admin)",
            color=discord.Color.blue()
            )

        await ctx.send(embed=embed)
   
    
def setup(bot):
    bot.add_cog(Help(bot))

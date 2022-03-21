import os
import json
import discord
import utils.utils as ut
from discord.ext import tasks, commands



class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.help = ut.readJSON(ut.directory['helpJSON'])
        self.helpParts = ""

    
    @commands.command(pass_context=True)
    async def help(self, ctx, *args):
        if not args: 
            self.helpParts = ""
            embed = discord.Embed(
                title="Main Commands",
                color=discord.Color.blue()
                )
            for i in self.help['shortHelp']: 
                embed.add_field(
                    name=f"{i['title']}", value=f"{i['text']}", inline=False)
        elif args[0]:
            if args[0] == "pillars":
                self.helpParts = ""
                     
                embed = discord.Embed(
                    title="Pillar Commands",
                    color=discord.Color.blue()
                    )
                for i in self.help['longHelp']['pillars']:
                    embed.add_field(
                        name=f"{i['title']}", value=f"{i['text']}", inline=False)
            
            elif args[0] == "admin":
                self.helpParts = ""
                    
                embed = discord.Embed(
                                title="Admin Commands",
                                color=discord.Color.blue()
                                )
                if ctx.author.id == 645688850500550677:
                    for i in self.help['longHelp']['admin']:
                        embed.add_field(
                            name=f"{i['title']}", value=f"{i['text']}", inline=False)
                else:
                    for i in self.help['longHelp']['admin']:
                        if i['owner'] == 0:
                            embed.add_field(
                                name=f"{i['title']}", value=f"{i['text']}", inline=False)
            else:
                embed = discord.Embed(
                            title="Wrong Context",
                            description=f"Please enter the right context of the commands",
                            color=discord.Color.blue()
                            )

        else:
            embed = discord.Embed(
                title="Wrong Context",
                description=f"Please enter the right context of the commands",
                color=discord.Color.blue()
            )
            
        await ctx.send(embed=embed)
            
   
    
def setup(bot):
    bot.add_cog(Help(bot))

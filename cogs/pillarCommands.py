import os
import json
import random
import discord
import utils.utils as ut
from discord.ext import tasks, commands
from dotenv import load_dotenv


class Pillars(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.sd = ut.readJSON(ut.directory['prefix'])
        self.pillars = ut.readJSON(ut.directory['pillarJSON'])
    
    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def prefix(self, ctx, prefix:str):
        response = ut.prefixCreation(ctx, prefix)
        if response['status'] == 1:
            self.bot = response['data']
            await ctx.send(f"prefix updated successfully")
        elif response['status'] == 2:
            self.bot = response['data']
            await ctx.send(f"the old and the new prefix are the same")
        else:
            await ctx.send(f"{response['data']}")    
        
    @commands.command(pass_context=True)
    async def pillar(self, ctx):
        # if string == "":
        
        random.shuffle(self.pillars['pillars'])
        random.shuffle(self.pillars['prefixes'])
        
        this = [[], []]
        this[0].append(self.pillars['pillars'][0]['pillarNum'])
        this[0].append(self.pillars['pillars'][0]['pillar'])
        this[0].append("Pillar")
        this[1].append(self.pillars['prefixes'][0]['prefixNum'])
        this[1].append(self.pillars['prefixes'][0]['prefix'])
        this[1].append("Prefix")
        random.shuffle(this)
        num = this[0][0]
        string1 = this[0][1]
        string2 = this[0][2]
        embed = discord.Embed(
            title=f"{string2} {num}",
            description=f"{string1}",
            color=discord.Color.green()
        )

        await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(Pillars(bot))

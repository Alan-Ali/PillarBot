import os
import json
import random
import discord
import utils.utils as ut
from discord.ext import tasks, commands


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
    async def pillars(self, ctx, *args):
        # if string == "":
        if not args:
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
        elif args: 
            if args[0] == 'prefix' and args[1].isnumeric():
                start, end, index = 1,10, 0
               
                num = int(args[1])
                print(type(num))
                if num and num >= start and num <= end:
                    string2 = "Prefix"
                    index = index + 1
                    for i in self.pillars['prefixes']:
                        if int(i['prefixNum']) == num:
                            string1 = i['prefix']
                            number = i['prefixNum']
                        index = index + 1
                    embed = discord.Embed(
                        title=f"{string2} {number}",
                        description=f"{string1}",
                        color=discord.Color.green()
                    )
                    await ctx.send(embed=embed)
            elif args[0] == 'pillar' and args[1].isnumeric():
                start, end,index = 1,80, 0
               
                num = int(args[1])
                print(type(num))
                if num and num >= start and num <= end:
                    string2 = "Pillar"
                    index = index + 1
                    for i in self.pillars['pillars']:
                        if int(i['pillarNum']) == num: 
                            string1 = i['pillar']
                            number = i['pillarNum']
                        index = index + 1
                    embed = discord.Embed(
                        title=f"{string2} {number}",
                        description=f"{string1}",
                        color=discord.Color.green()
                    )
                    await ctx.send(embed=embed)
            else:
                await ctx.send(f"Please enter the right commands in the right context")

def setup(bot):
    bot.add_cog(Pillars(bot))

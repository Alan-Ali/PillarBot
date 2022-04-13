import os
import json
import random
import discord
import utils.utils as ut
from discord.ext import tasks, commands


class Pillars(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.pillars = ut.readJSON(ut.directory['pillarJSON'])
        self.get_rand_channels = ut.readJSON(ut.directory['randChannel'])

    def randPillars(self):
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
        # return f"{string2} {num}\n{string1}"
        return embed
    
    @tasks.loop(seconds=3600.0)
    async def channelSet(self, arg):
        channel = self.bot.get_channel(id=int(arg))

        await channel.send(embed=self.randPillars())
        # print("hello")

    @commands.Cog.listener()
    async def on_ready(self):
        for i in self.get_rand_channels['randChannels']:
            self.channelSet.start(i['channel_rand'])

    @commands.command()
    async def setChannel(self, ctx, *args):
        # embed = discord.Embed()
        # await ctx.send("Say hello!")
        found_1, found_2, start = 0, False, 0
        end = len(args[0])
        # print(guild.channels)
        guild = self.bot.get_guild(ctx.guild.id)
        index = 0
        for channel in guild.channels:
            # print(channel.id)
            result = args[0].find(str(channel.id), start, end)
            if result != -1:
                found_1 = channel.id
                break
            index += 1
        print(found_1)
        # msg = await bot.wait_for("message")
        for i in self.get_rand_channels['randChannels']:
            if int(i['guild']) == int(ctx.message.guild.id):
                found_2 = True

        if found_2:
            return
        else:
            data = {
                "guild": int(ctx.message.guild.id),
                "channel_rand": int(found_1)
            }
            self.get_rand_channels['randChannels'].append(data)

            ut.updateJSON(ut.directory['randChannel'], self.get_rand_channels)

            return

    @commands.command(pass_context=True)
    async def pillars(self, ctx, *args):
        # if string == "":
        if not args:
            embed = self.randPillars()
            await ctx.send(embed=embed)
        elif args: 
            if args[0] == 'prefix' and args[1].isnumeric():
                start, end, index = 1,len(self.pillars['prefixes']), 0
               
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
                start, end, index = 1, len(self.pillars['pillars']), 0
               
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

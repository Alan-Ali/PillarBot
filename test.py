import os
import json
import discord
import utils.utils as ut
from discord.ext import tasks, commands
from dotenv import load_dotenv
import random




class Test(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.get_rand_channels = ut.readJSON(ut.directory['randChannel'])
        self.pillars = ut.readJSON(ut.directory[''])
        
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
                    title=f"{string2}",
                    description=f"{string1}",
                    color=discord.Color.green()
                )
        # return f"{string2} {num}\n{string1}"
        return embed


    @commands.command()
    async def test(self,ctx):
        # await ctx.send("this is it")
        # embed = discord.Embed(title="channels")
        text = ""
        
            # if len(text) < 1800:
            # embed.add_field(name="channel", value=f"<#{channel.id}>")
                # text += f"<#{channel.id}>\n"
        # await ctx.send(f"{text}")
                # text_channel_list.append(channel)

        # channel = discord.utils.get(bot.guild.channels)
        # channel_id = channel.id
        # print(text_channel_lis)




    @tasks.loop(seconds=5.0)
    async def channelSet(self,arg):
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
        found_1,found_2, start = 0, False,0
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
            index +=1
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
            


       
    


# async def update_member_count(ctx):
#     while True:
#         await ctx.send(ctx.guild.member_count)
#         channel = discord.utils.get(ctx.guild.channels, id=YourID)
#         await channel.edit(name=f'Member Count: {ctx.guild.member_count}')
#         await asyncio.sleep(TimeInSeconds)


# @bot.command()
# async def updatem(ctx):
#     bot.loop.create_task(update_member_count(ctx))  # Create loop/task
#     await ctx.send("Loop started, changed member count.")  # Optional

def setup(bot):
    bot.add_cog(Test(bot))










@commands.command()
async def getCategories(ctx):
    guild = discord.utils.get(ctx.guild.categories)
    print(len(ctx.guild.categories))
    print(len(ctx.guild.channels))
    print(len(ctx.guild.roles))

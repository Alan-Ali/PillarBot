import os
import json
import discord
import utils.utils as ut 
from discord.ext import tasks, commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = "OTU1MTc3OTI1MzA3NjYyMzg3.Yjd4ww.Jx-pt0Gn-p-6KWclS6w50dclv-4"


# here we are opeing the extensions file to get the extension details

# here prefixes to write down the prefix we need, will be replaced later


bot = commands.Bot(command_prefix="[", help_command=None)
bot.remove_command("help")  # for removing the main help command

# main function for loading other extensions
bot.load_extension(f"test")

bot.run(TOKEN)



import os
import json
import discord
import utils.utils as ut 
from discord.ext import tasks, commands
from dotenv import load_dotenv

load_dotenv()
GUILD = os.getenv('GUILD')
TOKEN = os.getenv('TOKEN')

# here we are opeing the extensions file to get the extension details
with open(ut.directory['extJSON']) as ext:
    extData = json.load(ext)
# here prefixes to write down the prefix we need, will be replaced later


bot = commands.Bot(command_prefix=ut.getPrefix, help_command=None)
bot.remove_command("help")  # for removing the main help command

# main function for loading other extensions
def main():
    
    # Assigning main extensions
    extensions = extData['extensions']
    # we go through each extension that we have of the cogs and load them
    for extension in extensions:
        ext = extension['extension']
        try:
            for folder in os.listdir("PillarBot"):
                if os.path.exists(os.path.join("PillarBot", folder, ext+".py")):
                    bot.load_extension(f"PillarBot.{folder}.{ext}")
                else:
                    bot.load_extension(f"cogs.{ext}")
        except Exception as errors:
            print(f'{ext} cannot be loaded. {errors}')

    bot.run(TOKEN)


if __name__ == '__main__':
    main()

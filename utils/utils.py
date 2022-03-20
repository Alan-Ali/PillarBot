import json
import discord
from discord.ext import tasks, commands

directory = {
    "prefix": './JSON/prefixes.json',
    "pillarJSON": './JSON/pillars.json',
    "pillarText": './data/pillarAddition.txt',
    "extJSON": "./JSON/extensions.json"
}

# directory = {
#     "prefix":  'PillarBot/JSON/prefixes.json',
#     "pillarJSON":  'PillarBot/JSON/pillars.json',
#     "pillarText":  'PillarBot/data/pillarAddition.txt',
#     "extJSON":  "PillarBot/JSON/extensions.json"
# }




def readText(directory):
    with open(directory, "r") as pre:
        pillars = pre
        pillarLines = pillars.readlines()
        return pillarLines


def readJSON(directory):
    with open(directory) as pre:
        return json.load(pre)


def updateJSON(directory, newData):
    with open(directory, "w") as oldData:
        json.dump(newData, oldData)


def getPrefix(client, message):
    prefixes = readJSON(directory['prefix'])
    allPrefixes = prefixes['prefixes']
    for i in allPrefixes:
        if i['guild'] == str(message.guild.id):
            return i['prefix']
        
    return allPrefixes[0]['prefix']


def prefixCreation(ctx, prefix):
    data = readJSON(directory['prefix'])
    prefixes = data['prefixes']
    if not " " in prefix:
        index = 0
        for i in prefixes:
            if str(ctx.guild.id) == i['guild']:
                if prefix != i['prefix']:
                    data['prefixes'][index]['prefix'] = prefix
                    
                    updateJSON(directory['prefix'], data)
                    status = {
                        "status": 1,
                        "data": commands.Bot(command_prefix=prefix)
                    }
                    return status
                elif prefix == i['prefix']: 
                    status = {
                    "status": 1,
                    "data": commands.Bot(command_prefix=i['prefix'])
                    }
                    return status
                else:
                    continue
            index = index + 1
            
        gid = str(ctx.guild.id)
        guildData = {
            "id": len(prefixes),
            "guild": gid,
            "prefix": prefix
        }
        data['prefixes'].append(guildData)
        updateJSON(directory['prefix'], data)
        print("here")
        status = {
            "status": 1,
            "data": commands.Bot(command_prefix=prefix)
        }
        return status
    else:
        status = {
            "status": 0,
            "data": f"Sorry, you used the wrong context, try again"
        }
        return status 


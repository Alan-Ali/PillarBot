import json
import utils as ut


pillars = ut.readText("./data/pillarAddition.txt")
# print(pillars[0])
Text = "".join(pillars)
allText = Text.split("&") 
prefixes = allText[0].split('%')
pillars = allText[1].split('%')
print(pillars[0])
pillarJSON = ut.readJSON("./JSON/pillars.json")

# print(pillarJSON)

for i in prefixes:
    parts = i.split("*")
    num = parts[0].split(":")[1]
    string = parts[1]
    data = {
        "prefixNum": int(num),
        "prefix": str(string)
    }

    pillarJSON['prefixes'].append(data)


for i in pillars: 
    parts = i.split("*")
    num = parts[0].split(":")[1]
    string = parts[1]
    data = {
        "pillarNum": int(num), 
        "pillar": str(string)
    }
    
    pillarJSON['pillars'].append(data)

ut.updateJSON("./JSON/pillars.json", pillarJSON)

    


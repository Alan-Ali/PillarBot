import json
import utils as ut


pillars = ut.readText(ut.directory['pillarText'])
# print(pillars[0])
Text = "".join(pillars)
allText = Text.split("&") 
prefixes = allText[0].split('%')
pillars = allText[1].split('%')
print(pillars[0])
pillarJSON = ut.readJSON(ut.directory['pillarJSON'])

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

ut.updateJSON(ut.directory['pillarJSON'], pillarJSON)

    


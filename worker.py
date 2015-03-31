import config
import htmlreader
import os

cat = htmlreader.categories
itm = htmlreader.itemNames
guideTitle = htmlreader.guideTitle
#guideTitle = 
title = htmlreader.title
champ = ""

for x in config.champions: 
	if x in title: champ = x

print("Champion: " + champ)

if champ not in config.folders:
	os.makedirs(config.folder + "\\" + champ + "\\Recommended")
else:
	if not os.path.exists(config.folder + "\\" + champ + "\\Recommended"):
		os.makedirs(config.folder + "\\" + champ + "\\Recommended")

currentFolder = config.folder + "\\" + champ + "\\Recommended\\"
print("Current folder: " + currentFolder)
json = '{"isGlobalForChampions":false,"associatedChampions":[],"mode":"any","blocks":[{"items":['

for x in range(0,len(itm)):
	json+='{"count":1,"id":"' + str(config.items[(itm[x])]) + '"},'
json = json[0:len(json)-1]
json += '], "type":"Items"}],"associatedMaps":[],"map":"any","title":"' + guideTitle + '","isGlobalForMaps":true,"sortrank":1,"type":"custom","champion":"' + champ + '","priority":false}'

print(json)
text_file = open(currentFolder + guideTitle.replace(" ", "_") + ".json", "w")
text_file.write(json)
text_file.close()


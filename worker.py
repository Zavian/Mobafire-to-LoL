import config
import beautifulsoupreader
import os


cat = beautifulsoupreader.categories
items = beautifulsoupreader.items
guideTitle = beautifulsoupreader.guideTitle
#guideTitle = 
title = beautifulsoupreader.title
champ = ""

def sanitize(s):
	s = s.replace("\\", " ")
	s = s.replace("/", " ")
	s = s.replace(":", " ")
	s = s.replace("*", " ")
	s = s.replace("?", " ")
	s = s.replace("\"", " ")
	s = s.replace("<", " ")
	s = s.replace(">", " ")
	s = s.replace("|", " ")
	return s

guideTitle = sanitize(guideTitle)

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
json = '{"isGlobalForChampions":false,"associatedChampions":[],"mode":"any","blocks":['

#for x in range(0,len(itm)):
#	json+='{"count":1,"id":"' + str(config.items[(itm[x])]) + '"},'

count = ""
for i in range(0, len(cat)):
	json += '{"items":['
	for item in items[i]:
		splitter = str(item).split(":")
		if len(splitter) > 1:
			item = splitter[0]
			count = splitter[1]
		if count != "":
			json += '{"count":'+ str(count) + ',"id":"' + str(item) + '"}'
		else: json += '{"count":1,"id":"' + str(item) + '"}'
		if items[i][-1] != item: json += ","
		count = ""
	json += '], "type":"' + cat[i] + '"'
	if cat[-1] != cat[i]: json += "},"

#for n in range(0, len(cat)):
#	print("cat: " + cat[n])
#	json += '{"items":['
#	for item in cat[n]:
#		json += '{"count":1,"id":"' + str(item) + '"}'
#		if cat[-1] != item:
#			json += ","
#
#	json += '], "type":"' + cat[n] + '"'
#	i += 1
#	if i < len(cat):
#		json += "},"

json = json[0:len(json)-1]
json += '"}],"associatedMaps":[],"map":"any","title":"' + guideTitle + '","isGlobalForMaps":true,"sortrank":1,"type":"custom","champion":"' + champ + '","priority":false}'

print()
print()
print()
print()
print(json)
text_file = open(currentFolder + guideTitle.replace(" ", "_") + ".json", "w")
text_file.write(json)
text_file.close()


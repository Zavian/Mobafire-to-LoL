from bs4 import BeautifulSoup
import config
import urllib.request
from urllib.request import urlopen
import utils

_DEBUG = True

def indexOf(string, search):
    return string.index(search)

def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')

site = config.site
connection = urllib.request.Request(site, headers=config.hdr)

# Parsing the whole page in a huge string
# and formatting it in utf-8
words = ""
for word in urlopen(connection).readlines():
    words += word.strip().decode('utf-8')

soup = BeautifulSoup(words)


# Extracting categories
categories = []
items = [[]]
#categories = {}
tCategories = soup.find_all(class_='item-wrap self-clear float-left')
for x in tCategories:
	#print(x.h2)
	if x.h2.string != None:
		#categories[x.h2.string.replace("\t", "")] = []
		categories.append(x.h2.string.replace("\t", ""))
	else:
		s = x.h2.contents[0]
		#categories[s.replace("\t", "")] = []
		categories.append(s.replace("\t", ""))


# Extracting item IDs
for x in range(0, len(categories)):
	tItems = tCategories[x].find_all(class_="main-items float-left  ")
	#print(tItems)
	items.append([])
	for r in tItems:
		tmp = r.find_all(class_="item-title")
		#item = tmp[0].span["class"][1]
		#item = item[len("{t:'Item',i:'"):].replace("'}", "")
		item = tmp[0].span.string
		#print(tmp[0].span.string)
		tmpCount = r.find_all(class_="hiliteW")
		if len(tmpCount) > 0:
			count = tmpCount[0].string
			count = count.replace("x", "")
			item = config.items[item]
			item = str(item) + ":" + count
			items[x].append(item)
		else: items[x].append(config.items[item])


tTitle = soup.title
title = tTitle.string

tGuideTitle = soup.find(class_="build-title")
guideTitle = tGuideTitle.h2.string

if _DEBUG:
	print("Title: " + title)
	print("Guide Title: " + guideTitle)
	utils.printArrayDebug(categories, "Categories")
	utils.printArrayDebug(items, "Items")
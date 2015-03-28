import config
import utils
#import main
import urllib.request
from html.parser import HTMLParser
from urllib.request import urlopen


_DEBUG = True

catOffsets = []
iteOffsets = []
titOffset = []

datas = []

categories = []
itemIDs = []
itemNames = []

#if "url" in main.final: site = main.url
#elif "champion" in main.final: pass # Gotta make the list of all the heroes

def indexOf(string, search):
    return string.index(search)

class MyHTMLParser(HTMLParser):
    # Globals
    findIteEnd = False
    findCatEnd = False
    findTitEnd = False

    # Definitions
    def handle_starttag(self, tag, attrs):
        if tag == "h2":
            if any("guide-main-title" in s for s in attrs):
                linen, offset = self.getpos()
                titOffset.append(offset)
                findTitEnd = True

        if tag == "div":
            if any("item-wrap self-clear float-left" in s for s in attrs):
                linen, offset = self.getpos()
                catOffsets.append(offset)
                self.findCatEnd = True
            if any("main-items float-left  " in s for s in attrs):
               linen, offset = self.getpos()
               iteOffsets.append(offset)
               self.findIteEnd = True

    def handle_endtag(self, tag):
        if self.findIteEnd: 
            linen, offset = self.getpos()
            iteOffsets[-1] = str(iteOffsets[-1]) + " " + str(offset)
            self.findIteEnd = False
            datas.append(self.get_starttag_text())

        if self.findCatEnd:
            linen, offset = self.getpos()
            catOffsets[-1] = str(catOffsets[-1]) + " " + str(offset)
            self.findCatEnd = False

        if self.findTitEnd:
            linen, offset = self.getpos()
            titOffset[-1] = str(titOffset[-1]) + " " + str(offset)
            self.findTitEnd = False;


# Connection stuff
site = "http://www.mobafire.com/league-of-legends/build/xerath-the-magus-ascendent-392279"
connection = urllib.request.Request(site, headers=config.hdr)

# Parsing the whole page in a huge string
# and formatting it in utf-8
words = ""
for word in urlopen(connection).readlines():
    words += word.strip().decode('utf-8')

parser = MyHTMLParser()
parser.feed(words) # Feeding the parser with the string

# Now I have all the offsets
for x in catOffsets:
    Osup = int(x.split(' ')[0]) + len('<div class="item-wrap self-clear float-left"><h2>')  # This will delete the first part of the string
    Oinf = int(x.split(' ')[1]) 
    ind = indexOf(words[Osup:Oinf], '\t') # This will let me to delete all tabulations in the string
    if ind != None:
        Oinf = Osup + ind
    categories.append(words[int(Osup):int(Oinf)])
    if _DEBUG: print(words[int(x.split(' ')[0]):int(x.split(' ')[1])]) # Debug





for x in iteOffsets:
    # Same as for b4
    Osup = int(x.split(' ')[0]) + len('<div class="main-items float-left  "><a href="/league-of-legends/item/')
    Oinf = int(x.split(' ')[1])

    ind = indexOf(words[Osup:Oinf], "i:")
    Osup += ind + len("i:'")
    Oinf -= len("'}\">")
    itemIDs.append(words[int(Osup):int(Oinf)])
    if _DEBUG: print(words[int(x.split(' ')[0]):int(x.split(' ')[1])]) # Debug

for x in datas:
    Osup = indexOf(x, "alt=") + len("alt='")
    Oinf = len(x) - len('" LoL />')
    itemNames.append(x[Osup:Oinf])
    if _DEBUG: print(x[Osup:Oinf]) # Debug


#print(titOffset[0])

ind = indexOf(words[(titOffset[0] + 1):], "/h2>")
title = words[titOffset[0] + len('<h2 class="guide-main-title">'):titOffset[0] + ind]

if _DEBUG: 
    utils.printDebug(categories, "Categories")
    utils.printDebug(itemIDs, "Item IDs")
    utils.printDebug(itemNames, "Item Names")
    print("Title: " + title)



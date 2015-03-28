# Mobafire-to-LoL

This application will let you easily import any guide from mobafire.com into the ingame guide system of League of Legends.
You'll just need to provide a link (example: http://www.mobafire.com/league-of-legends/build/xerath-the-magus-ascendent-392279)
and the program will parse it into a json file into the right directory.

# Usage
Just compile the file worker.py with Python 3. 

**Remember to change the value of the variable "folder" into the config.py file**

> Example: "C:\Program Files (x86)\Riot Games\League of Legends\Config\Champions\"

*Right now you will have to change manually the variable "site" into the file "htmlreader.py" although this is just temporary*

# Todo
- Create a local database of default guides
- Create a GUI
- Make possible to search through various guides
- Creating automatically the categories
- Displaying the suggested number of items to buy
- Various

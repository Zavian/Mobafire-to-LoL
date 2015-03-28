import config


command = input("Insert your command: ")

final = {}


# Cheat sheet for the commands:
# 	INSTALL 		: Install every hero
#	INSTALL [hero]	: Install hero
#	INSTALL [url]	: Install mobafire url
l = len("INSTALL")
if command[0:l] == "INSTALL":
	args = command[l:]
	if args != "" or args != None:
		args = args.strip()
		if args != "":
			ind = None
			try:
				ind = args.index("http://")
			except Exception:
				pass
			if ind != None:
				final["url"] = args
			elif args in config.champions:
				final["champion"] = args



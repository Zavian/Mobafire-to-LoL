def printArrayDebug(array, name):
    print("Printing " + name)
    for x in array: 
    	print("\t", end="")
    	print(x)
    print("End " + name)
    print()

def printDictionaryDebug(dictionary, name):
	print("Printing " + name)
	for x in dictionary: 
		print("\t" + x, end="\n\t")
		print(dictionary[x])
		print()
	print("End " + name)
	print()

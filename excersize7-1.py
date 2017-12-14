fname = input("Enter the file name: ")
try:
	fhand = open(fname)
except:
	print("The file " + fname + " cannot be opened, sorry about that")
	exit()
for line in fhand:
	str.capitalize(line)
	print(line)
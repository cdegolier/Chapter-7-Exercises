fname = input("Enter the file name: ")
#easter egg that displays 'na na boo boo yall been punked'
if fname == 'na na boo boo':
	print ("HA YALL BEEN PUNKED")
	exit()

#trys to open the named file and displays error message if doesnt exist
try:
	fhand = open(fname)
except:
	print("The file " + fname + " cannot be opened, sorry about that")
	exit()

for line in fhand:
	str.capitalize(line)
	print(line)
import sys


dir = "/home/jiri/ownCloud/notes/"

load = open("/home/jiri/ownCloud/notes/"+"todo.md","r+")
lines = load.readlines()



if len(sys.argv) < 2: #name of program is 1
	for line in lines:
		if line.find("[]") > 0:
			print line
	if len(lines) < 1:
		print "there are no todos yet... please use 'add' "
		last = 0
	else:
		last = len(lines)+1
else:
	usr_type = sys.argv[1]
	if len(lines) < 1: 
		last = 0 
	else:
		last = len(lines)+1
	
	if usr_type == "add":
		last = last + 1
		usr_input = " ".join(sys.argv[2:]) 
		load.write("("+str(last)+")[] "+usr_input+"\n")
	if usr_type == "done":
		usr_done = sys.argv[2]
		for line in lines:
			if line.find("("+usr_done+")") > 0:
				line.replace("[]","[x]")


load.close()

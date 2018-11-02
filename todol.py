#!/usr/bin/python3
import os
import sys
import time
#(6)[]  check new lines and if they dont have (id)[] added it
#2018-11-02 add info command to write how many todos there are etc

# Set directory
dir = "/home/jiri/ownCloud/notes/"

def backup(lines,dir):
	print("Do you want to creat backup? (yes/no)")
	usr_confirmation_backup = input()
	if usr_confirmation_backup in ['y','Y','yes','YES']:
		backup = open(dir+"todo_backup_"+str(time.time())+".md","w")
		backup.writelines(lines)
		backup.close()
	return

if os.path.isfile(dir+"todo.md") == False:
	print("There is no todo.md file. Do you want to creat it in directory: "+dir+"? (yes/n)")
	usr_create_file = input()
	if usr_create_file in ['y','Y','yes','YES']:
		create = open(dir+"todo.md","w")
		create.close()
	else: 
		sys.exit()

load = open(dir+"todo.md","r")
lines = load.readlines()
load.close()


if len(sys.argv) < 2: #name of program is 1
	found_line = 0
	for line in lines:
		if line.find("[]") > 0:
			print(line)
			found_line = 1
	if len(lines) < 1 or found_line==0:
		print("there are no todos yet... please use 'add' ")
		last = 0
	else:
		last = len(lines)+1
else:
	usr_type = sys.argv[1]
	if len(lines) < 1: 
		last = 0 
	else:
		last = len(lines)+1
	
	if usr_type in ["add","+"]:
		last = last + 1
		usr_input = " ".join(sys.argv[2:]) 
		lines.insert(0,("("+str(last)+")[] "+usr_input+"\n"))
	if usr_type == "done":
		for usr_done in sys.argv[2:]:
			found_done = 0
			for i in range(0,len(lines)):
				if lines[i].find("("+usr_done+")[]") != -1:
					lines[i] = lines[i].replace(")[]",")[x]")
					print(lines[i])
					found_done = 1
			if found_done == 0: 
				print("To do "+usr_done+" not found or already done")
			elif found_done ==1:
				print("To-do "+usr_done+" done")



	if usr_type == "clear":
		backup(lines,dir)
		print("Are you sure to delete all to-dos? (yes/no)")
		usr_confirmation_clear = input()
		if usr_confirmation_clear in ['y','Y','yes','YES']:
			lines = ""
	if usr_type == "backup":
		backup(lines,dir)
		

load = open(dir+"todo.md","w")
load.seek(0)
load.writelines(lines)
load.truncate()
load.close()


#!/usr/bin/python3
import os
import sys
import time
import readline
import pickle
#(6)[]  check new lines and if they dont have (id)[] added it
#2018-11-02 add info command to write how many todos there are etc


	





def backup(lines,dir):
	print("Do you want to creat backup? (yes/no)")
	usr_confirmation_backup = input()
	if usr_confirmation_backup in ['y','Y','yes','YES']:
		backup = open(dir+"todo_backup_"+str(time.time())+".md","w")
		backup.writelines(lines)
		backup.close()
	return

def input_with_prefill(prompt, text):
    def hook():
        readline.insert_text(text)
        readline.redisplay()
    readline.set_pre_input_hook(hook)
    result = input(prompt)
    readline.set_pre_input_hook()
    return result


# Set directory
dir = "/home/jiri/ownCloud/notes/"
dir_script = sys.path[0]

if os.path.isfile(dir_script+"/objs.pkl")==False:
	dir = input_with_prefill("Set path to todo.md:", dir)
	with open(dir_script+'/objs.pkl', 'wb') as f:
    		pickle.dump(dir, f)

with open(dir_script+'/objs.pkl', "rb") as f: 
    dir = str(pickle.load(f))




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
	if len(lines) < 1:
		print("there are no todos yet... please use 'add' ")
		last = 0
	else:
		last = len(lines)+1

	found_line = 0
	for l in range(0, len(lines)):
		if lines[l].find(")[]") == -1 and lines[l].find(")[x]") == -1:
			print(lines[l]+"Do you want to add ID and checkbox?:")
			usr_auto = input()
			if usr_auto in ["y","Y","yes","YES"]:
				lines[l] = "("+str(last)+")[]"+lines[l]
				last = last + 1
	print("---------------")
	for j in range(0, len(lines)):
		if lines[j].find(")[]") > 0:
			print(lines[j])
			found_line = 1			
	if found_line == 0:
		print("All todos are already done... please use 'add'") 
	print("---------------")
else:
	usr_type = sys.argv[1]
	if len(lines) < 1: 
		last = 0 
	else:
		last = len(lines)+1
	
	if usr_type in ["add","+","a"]:
		last = last + 1
		usr_input = " ".join(sys.argv[2:]) 
		lines.insert(0,("("+str(last)+")[] "+usr_input+"\n"))
	elif usr_type in ["done","d"]:
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
	elif usr_type in ["e","edit"]:
		for usr_done in sys.argv[2:]:
			found_done = 0
			for i in range(0,len(lines)):
				if lines[i].find("("+usr_done+")[]") != -1:
					lines[i] = input_with_prefill("Edit:",lines[i]).rstrip()+"\n"
					found_done = 1
			if found_done == 0: 
				print("To do "+usr_done+" not found")



	elif usr_type == "clear":
		backup(lines,dir)
		print("Are you sure to delete all to-dos? (yes/no)")
		usr_confirmation_clear = input()
		if usr_confirmation_clear in ['y','Y','yes','YES']:
			lines = ""
	elif usr_type == "backup":
		backup(lines,dir)
	elif usr_type in ["help","h"]:
		print("------------- \n add [text] - to add new todo \n edit [id] - edite todos \n done [id] - mark as done \n clear - to clear all todos in file \n backup - backup in new file \n-------------")
	else:
		last = last + 1
		usr_input = " ".join(sys.argv[1:]) 
		lines.insert(0,("("+str(last)+")[] "+usr_input+"\n"))
		

load = open(dir+"todo.md","w")
load.seek(0)
load.writelines(lines)
load.truncate()
load.close()


#!/usr/bin/python3
import os
import sys
import time
import readline
import pickle
from colored import fg, bg, attr

# Colour setting
cl_header = fg(72)
cl_checkbox = fg(125)
cl_message = fg(125)
cl_number = fg(78)
cl_sepparator = fg(166) 
cl_reset = attr('reset')
#cl_header = fg('#2AA198')
#cl_checkbox = fg('#D33682')
#cl_number = fg('#106E1E')
#cl_sepparator = fg('#0B4D5E')

def backup(lines,dir,todo):
    print("Do you want to create backup? (yes/no)")
    usr_confirmation_backup = input()
    if usr_confirmation_backup in ['y','Y','yes','YES']:
        if not os.path.exists(dir+"backup/"):
               os.makedirs(dir+"backup/")
        backup = open(dir+"backup/"+todo+"backup_"+str(time.time())+".md","w")
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

def isFileType(s):
    if s.endswith("_tdl.md"):
        return True
    else: 
        return False
def printID(x):
    if x < 10:
        return "("+str(x)+")  "
    elif x >= 10 & x < 100:
        return "("+str(x)+") "
    else:
        return "("+str(x)+")"

def printToDo(j, checked = True):
    if checked == False:
        print(cl_number + printID(j) + cl_reset + cl_checkbox + "[ ]" + cl_reset + lines[j].replace("- [ ]", ""), end="")
    else:
        print(cl_number + printID(j) + cl_reset + cl_checkbox + "[X]" + cl_reset + lines[j].replace("- [X]", ""), end="")

def sep():
    print(cl_sepparator + "----------------------" + cl_reset)

# Set directory
dir = "/home/jiri/ownCloud/notes/"
todo = "todo_tdl.md"
dir_script = sys.path[0]

if os.path.isfile(dir_script+"/objs.pkl")==False:
    dir = input_with_prefill("Set path to todo list file:", dir)
    todo = input_with_prefill("Default file (recommended: 'todo_tdl.md'):", todo)
    todo_open = todo
    with open(dir_script+'/objs.pkl', 'wb') as f:
         pickle.dump([dir, todo, todo_open], f)

with open(dir_script+'/objs.pkl', "rb") as f: 
    dir, todo, todo_open = pickle.load(f)




if os.path.isfile(dir+todo_open) == False:
    print("There is no "+todo_open+" file. Do you want to create it in directory: "+dir+"? (yes/n)")
    usr_create_file = input()
    if usr_create_file in ['y','Y','yes','YES']:
            create = open(dir+todo_open,"w")
            create.close()
    else: 
            todo_open = todo
            with open(dir_script+'/objs.pkl', 'wb') as f:
                pickle.dump([dir, todo, todo_open], f)
            sys.exit()

load = open(dir+todo_open,"r")
lines = load.readlines()
load.close()


if len(sys.argv) < 2: #name of program is 1
    list_of_notes = filter(isFileType,os.listdir(dir))
    sep()
    print(cl_header + "file: "+todo_open+" | "+str(list(list_of_notes)) + cl_reset)
    if len(lines) < 1:
            sep()
            print("there are no todos yet... please use 'add' ")
            last = 0
    else:
            last = len(lines)+1

    found_line = 0
# CHECK FOR CHECKBOX
    if todo_open.find("_tdl.md") > 0:
        for l in range(0,len(lines)):
            if lines[l].find("- [ ]") == -1 and lines[l].find("- [X]") == -1:
                print(lines[l]+"Do you want to add checkbox?:")
                usr_auto = input()
                if usr_auto in ["y","Y","yes","YES"]:
                            lines[l] = "- [ ] "+lines[l]
    sep()
# PRINT TODOs
    for j in range(0, len(lines)):
        if lines[j].find(" [ ] ") > 0:
            printToDo(j, False)
            found_line = 1			
    if found_line == 0 and len(lines)>1:
        print("All to-do are already done... please use 'add'") 
    sep()
else:
    usr_type = sys.argv[1]
# ADD
    if usr_type in ["-add","+","-a"]:
        usr_input = " ".join(sys.argv[2:]) 
        lines.insert(0,("- [ ] "+usr_input+"\n"))
# INSERT
    if usr_type in ["-insert","-i"]:
        insert_position = int(sys.argv[2]) 
        usr_input = " ".join(sys.argv[3:]) 
        lines.insert(insert_position,("- [ ] "+usr_input+"\n"))
# PRINT ALL
    elif usr_type in ["-all"]:
        for j in range(0, len(lines)):
            if lines[j].find(" [ ] ") > 0:
                printToDo(j, False)    
            elif lines[j].find(" [X] ") > 0:
                printToDo(j, True)
        print("\n")
        sep()
# DONE
    elif usr_type in ["-done","-d"]:
        for usr_done in sys.argv[2:]:
            if int(usr_done) > len(lines):
                print("To do "+usr_done+" does not exist")
            elif lines[int(usr_done)].find("- [X]") == 2:
                print("To do "+cl_number+usr_done+cl_reset+" not found or already done")
            else:
                lines[int(usr_done)] = lines[int(usr_done)].replace("- [ ]","- [X]")
                print("To-do "+cl_number+usr_done+cl_reset+" done")
# UNDONE
    elif usr_type in ["-udone","-u"]:
        for usr_undone in sys.argv[2:]:
            if int(usr_undone) > len(lines):
                print(cl_message + "To do "+ cl_reset + cl_number +usr_undone+cl_reset+" does not exist")
            elif lines[int(usr_undone)].find(")[ ]") == 2:
                print(cl_message + "To do " + cl_reset + cl_number +usr_undone+cl_reset+" is in progress")
            else:
                lines[int(usr_undone)] = lines[int(usr_undone)].replace("- [X]","- [ ]")
                print(cl_message + "To-do "+ cl_reset + cl_number +usr_undone+ cl_reset+ " undone")
# EDIT
    elif usr_type in ["-e","-edit"]:
        for usr_edit in sys.argv[2:]:
            if int(usr_edit) > len(lines):
                print("To do"+cl_number+usr_edit+cl_reset+" does not exist")
            else:
                print(cl_message+"Edit: "+cl_reset)
                lines[int(usr_edit)] = input_with_prefill(":",lines[int(usr_edit)]).rstrip()+"\n"
# CLEAR
    elif usr_type == "-clear":
        backup(lines,dir,todo_open)
        print("Are you sure to delete all to-dos? (yes/no)")
        usr_confirmation_clear = input()
        if usr_confirmation_clear in ['y','Y','yes','YES']:
            lines = ""
# BACKUP
    elif usr_type == "-backup":
        backup(lines,dir,todo_open)
# HELP
    elif usr_type in ["-help","-h"]:
        sep()
        print(" add [text] - to add new todo \n edit [id] - edit todos \n done [id] - mark as done \n clear - to clear all todos in file \n backup - backup in new file ")
        sep()
# SWITCH FILE
    elif usr_type in ["-switch", "-s"]:
        switch = sys.argv[2]
        if switch == "-l":
            list_of_notes = filter(isFileType,os.listdir(dir))
            print(str(list(list_of_notes)))
        elif os.path.isfile(dir+switch+".md")==False:
            print("There is no "+cl_message +switch+".md"+cl_reset+" file to switch to. Do you want to create it in directory: "+dir+"? (yes/no)")
            usr_create_file = input()
            if usr_create_file in ['y','Y','yes','YES']:
                create = open(dir+switch+".md","w")
                create.close()
                todo_open = switch+".md"
                with open(dir_script+'/objs.pkl', 'wb') as f:
                    pickle.dump([dir, todo, todo_open], f)
                sys.exit()
            else: 
                sys.exit()
        else:
            todo_open = switch+".md"
            with open(dir_script+'/objs.pkl', 'wb') as f:
                    pickle.dump([dir, todo, todo_open], f)
            sys.exit()
# SWITCH TO MAIN
    elif usr_type in [".."]:
        todo_open = todo
        with open(dir_script+'/objs.pkl', 'wb') as f:
                pickle.dump([dir, todo, todo_open], f)
        sys.exit()
    else:
        usr_input = " ".join(sys.argv[1:]) 
        lines.insert(0,("- [ ] "+usr_input+"\n"))


load = open(dir+todo_open,"w")
load.seek(0)
load.writelines(lines)
load.truncate()
load.close()


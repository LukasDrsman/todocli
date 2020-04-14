#!/usr/bin/python3
from functions import *

# init
if(os.path.isfile(path) != True):
    notes = open(path, "w")
    notes.close()

todolist = load(path)
show(todolist)

# main loop
while(1):
    usrInput = input(prompt)
    if(" " in usrInput):
        command, parameter = usrInput.split(' ', 1)
    else:
        command = usrInput
        parameter = ""

    if(command == "new" or command == "n"):
        new(todolist, parameter)
        show(todolist)

    elif(command == "write" or command == "w"):
        save(todolist, path)

    elif(command == "load" or command == "l"):
        todolist = load(path)
        show(todolist)

    elif(command == "check" or command == "cc"):
        check(todolist, parameter)
        show(todolist)

    elif(command == "uncheck" or command == "uc"):
        uncheck(todolist, parameter)
        show(todolist)

    elif(command == "quit" or command == "q" or command == "exit" or command == "x"):
        if(writeonexit == True):
            save(todolist, path)
        print("\033c", end="")
        exit()

    elif(command == "clear" or command == "cl"):
        delete()
        todolist = load(path)
        show(todolist)

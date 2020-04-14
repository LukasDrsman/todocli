#!/usr/bin/python3
from functions import *

if(os.path.isfile(path) != True):
    notes = open(path, "w")
    notes.write(title + "\n")
    notes.close()

show()
while (1):
    usrInput = input(prompt)
    if (" " in usrInput):
        command, parameter = usrInput.split(' ', 1)
    else:
        command = usrInput
        parameter = ""
    if (command == "new" or command == "n"):
        new(parameter)
        show()
    if (command == "check" or command == "cc"):
        check(parameter)
        show()
    if (command == "uncheck" or command == "uc"):
        uncheck(parameter)
        show()
    if (command == "quit" or command == "q"):
        print("\033c", end="")
        exit()
    if (command == "exit" or command == "x"):
        print("\033c", end="")
        exit()
    if (command == "clear" or command == "l"):
        delete()
        show()

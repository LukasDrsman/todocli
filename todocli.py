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
    if (command == "check" or command == "cc"):
        check(parameter)
    if (command == "uncheck" or command == "uc"):
        uncheck(parameter)
    if (command == "quit" or command == "q"):
        exit()
    if (command == "exit" or command == "x"):
        exit()
    if (command == "clear" or command == "l"):
        delete()
    show()

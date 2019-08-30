import sys
import os
from config import *
from os.path import expanduser

path = os.path.expanduser(notes_path)
hlp = os.path.expanduser(hlp_path)


def show():
    os.system('clear')
    data = open(path, "r")
    print(data.read())
    data.close()


def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()


def check(a):
    ln = int(a)
    f = open(path, "r")
    lines = f.readlines()
    f.close()
    swap = lines[ln]
    cchar = list(swap)
    cchar[1] = finished
    joined = "".join(cchar)
    prntable = str(joined)
    print(prntable)
    replace_line(path, ln, prntable)


def uncheck(y):
    x = int(y)
    f = open(path, "r")
    lines = f.readlines()
    f.close()
    swap1 = lines[x]
    cchar1 = list(swap1)
    cchar1[1] = unfinished
    joined1 = "".join(cchar1)
    prntable1 = str(joined1)
    print(prntable1)
    replace_line(path, x, prntable1)


def readall():
    data = open(path, "r")
    print(data.read())
    data.close()


def new(newin):
    notes = open(path, "a")
    newnote = " "+unfinished+" "+newin
    notes.write(newnote+"\n")
    notes.close()


def delete():
    yon = input("Do you want to delete current TODO list? ([y]es or [n]o) ")
    if (yon == "y" or yon == "Y" or yon == "yes"):
        note = open(path, "w")
        note.write("")
        note.close()
        todo = open(path, "w")
        todo.write(title + "\n")
        todo.close()


def read_help():
    pathto = open(hlp, "r")
    print(pathto.read())
    pathto.close()


while (1):
    usrInput = input("~ ")
    if (" " in usrInput):
        command, parameter = usrInput.split(' ')
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
    if (command == "delete" or command == "del"):
        delete()
    if (command == "read" or command == "r"):
        readall()
    if (command == "show" or command == "s"):
        show()
    if (command == "help" or command == "h"):
        read_help()

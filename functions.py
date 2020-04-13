import os
from config import *
from os.path import expanduser, isfile

path = os.path.expanduser(notes_path)

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

def check(i):
    ln = int(i)
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

def uncheck(i):
    ln = int(i)
    f = open(path, "r")
    lines = f.readlines()
    f.close()
    swap = lines[ln]
    cchar = list(swap)
    cchar[1] = unfinished
    joined = "".join(cchar)
    prntable = str(joined)
    print(prntable)
    replace_line(path, ln, prntable)

def new(newin):
    notes = open(path, "a")
    newnote = " "+unfinished+" "+newin
    notes.write(newnote+"\n")
    notes.close()


def delete():
    yon = input("Do you want to delete current TODO list? ([y]es or [n]o) ")
    if (yon == "y" or yon == "Y" or yon == "yes"):
        notes = open(path, "w")
        notes.write("")
        notes.write(title + "\n")
        notes.close()

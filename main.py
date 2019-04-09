import sys
import os

unfinished = "□"
finished = "■"
path = "/home/lukas/python/notes/notes.txt"
hlp = "/home/lukas/python/notes/help.txt"

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

def check(ln):
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

def uncheck(x):
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

def new():
    notes = open(path, "a")
    newin = input(">> ")
    newnote = " "+unfinished+" "+newin
    notes.write(newnote+"\n")
    notes.close()

def delete():
    yon = input("Do you want to delete current TODO list? ([y]es or [n]o)")
    if (yon == "y" or yon == "Y" or yon == "yes"):
        note = open(path, "w")
        note.write("")
        note.close()
        todo = open(path, "w")
        todo.write("TODO: \n")
        todo.close()

def main():
    while (1):
        inputsh = input("- ")
        if (inputsh == "show" or inputsh == "s"):
            show()
        if (inputsh == "new" or inputsh == "n"):
            new()
        if (inputsh == "exit" or inputsh == "q"):
            exit()
        if (inputsh == "delete" or inputsh == "del"):
            delete()
        if (inputsh == "read" or inputsh == "r"):
            readall()
        if (inputsh == "help" or inputsh == "h"):
            os.system('clear')
            help = open(hlp, "r")
            print(help.read())
            help.close()
        if (inputsh == "check" or inputsh == "cc"):
            choose = int(input(">> "))
            if (choose >= 1):
                check(choose)
        if (inputsh == "uncheck" or inputsh == "uc"):
            unchoose = int(input(">> "))
            if (unchoose >= 1):
                uncheck(unchoose)
main()

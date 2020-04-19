import os
from config import *
from os.path import expanduser, isfile
from datetime import datetime

END = '\033[0m'
todate = datetime.today()

# path to name_of_todolist.todolist (defined in config.py)
path = os.path.expanduser(notes_path)

# default task state flags
flags.append((("cc", "check"), ("■", "1"), (GREY, True)))
flags.append((("uc", "uncheck"), ("□", "0"), (NONE, False)))

def change_flag(todo, command, n):
    try:
        tasknum = int(n) - 1
    except:
        tasknum = len(todo) + 1
    for i in range(len(flags)):
        if(flags[i][0][0] == command or flags[i][0][1] == command):
            try:
                todo[tasknum][1] = flags[i][1][1]
            except:
                pass

# load todolist to python list
def load(path):
    list = []
    file = open(path, 'r')
    lines = file.readlines()
    for i in range(len(lines)):
        try:
            task, state, duedate = (lines[i].rstrip("\n")).split("|")
            due = datetime.strptime(duedate, '%Y-%m-%d')
            list.append([task, state, due])
        except:
            task, state = (lines[i].rstrip("\n")).split("|")
            list.append([task, state, "none"])
    return list

# print todolist from python list
def show(todo):
    print("\033c", end="")
    if(showtitle == True):
        print(title)
    for i in range(len(todo)):
        for y in range(len(flags)):
            if(flags[y][1][1] == todo[i][1]):
                taskinfo = flags[y][1][0]+" "+todo[i][0]
                if(showdeadline == False):
                    if(type(todo[i][2]) is datetime):
                        if(todo[i][2] >= todate):
                            print(flags[y][2][0]+taskinfo+END)
                        elif(todo[i][2] < todate and flags[y][2][1] == True):
                            print(flags[y][2][0]+taskinfo+END)
                        else:
                            print(RED+taskinfo+END)
                    else:
                        print(flags[y][2][0]+taskinfo+END)
                if(showdeadline == True):
                    if(type(todo[i][2]) is datetime):
                        if(todo[i][2] >= todate):
                            print(flags[y][2][0]+taskinfo+END+" "+" → "+todo[i][2].strftime('%a %d %b'))
                        elif(todo[i][2] < todate and flags[y][2][1] == True):
                            print(flags[y][2][0]+taskinfo+END+" "+" → "+todo[i][2].strftime('%a %d %b'))
                        else:
                            print(RED+taskinfo+END+" "+" → "+todo[i][2].strftime('%a %d %b'))
                    else:
                        print(flags[y][2][0]+taskinfo+END)
                break
    print(" ")

# save changes to todolist file
def save(todo, path):
    file = open(path, 'w')
    file.write("")
    file.close()
    file = open(path, 'a')
    for i in range(len(todo)):
        if(type(todo[i][2]) is datetime):
            file.write(todo[i][0]+"|"+todo[i][1]+"|"+todo[i][2].strftime('%Y-%m-%d')+"\n")
        else:
            file.write(todo[i][0]+"|"+todo[i][1]+"\n")

# create new task (in todolist python list)
def new(todo, task):
    todo.append([task, "0", "none"])

def cdate(todo, n):
        try:
            tasknum = int(n) - 1
        except:
            tasknum = len(todo) + 1
        duedate = input("(Year month day) "+promptcol+prompt+END)
        try:
            due = datetime.strptime(duedate, '%Y %m %d')
        except:
            due = "none"
        todo[tasknum][2] = due

def remove(todo, n):
        try:
            tasknum = int(n) - 1
        except:
            tasknum = len(todo) + 1
        try:
            todo.pop(tasknum)
        except:
            pass

# clear the todolist file
def delete():
    consent = input("Are you sure yu want to clear your todolist?\n([y]es or [n]o) "+promptcol+prompt+END)
    if (consent == "y" or consent == "Y" or consent == "yes"):
        file = open(path, "w")
        file.write("")
        file.close()

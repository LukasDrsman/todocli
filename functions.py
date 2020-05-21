import os
from config import *
from os.path import expanduser, isfile
from datetime import datetime

# TODO: task descriptions
# TODO: sort:
# TODO:     sort by datetime
# TODO:     sort by priority

todate = datetime.today()
path = os.path.expanduser(defpath)
ddir = os.path.expanduser(defdir)

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

def load(path):
    list = []
    file = open(path, 'r+')
    pretitle, mess = str(os.path.basename(file.name)).split(".")
    title = pretitle+": "
    lines = file.readlines()
    for i in range(len(lines)):
        try:
            task, state, duedate = (lines[i].rstrip("\n")).split("|")
            due = datetime.strptime(duedate, '%Y-%m-%d')
            list.append([task, state, due])
        except:
            task, state  = (lines[i].rstrip("\n")).split("|")
            list.append([task, state, "none"])
    return list, title

def show(todo, title):
    print("\033c", end="")
    if(showtitle == True):
        print(title)
    for i in range(len(todo)):
        if(linenum == True):
            num = i + 1
            print(linenumformat % num, end="")
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
                            print(flags[y][2][0]+taskinfo+END+" "+" → "+todo[i][2].strftime(dateformat))
                        elif(todo[i][2] < todate and flags[y][2][1] == True):
                            print(flags[y][2][0]+taskinfo+END+" "+" → "+todo[i][2].strftime(dateformat))
                        else:
                            print(RED+taskinfo+END+" "+" → "+todo[i][2].strftime(dateformat))
                    else:
                        print(flags[y][2][0]+taskinfo+END)
                break
    print(" ")

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

def new(todo, task):
    todo.append([task, deflag, "none"])

def change_date(todo, n):
        try:
            tasknum = int(n) - 1
        except:
            tasknum = len(todo) + 1

        if(thisyear == False):
            duedate = input("(Year month day) "+promptcol+prompt+END)
        else:
            duedate = input("(month day) "+promptcol+prompt+END)
        try:
            if(thisyear == False):
                due = datetime.strptime(duedate, '%Y %m %d')
            else:
                year = datetime.now().strftime('%Y')
                due = datetime.strptime(year + " " + duedate, '%Y %m %d')
        except:
            due = "none"
        try:
            todo[tasknum][2] = due
        except:
            pass

def remove(todo, n):
        try:
            tasknum = int(n) - 1
        except:
            tasknum = len(todo) + 1
        try:
            todo.pop(tasknum)
        except:
            pass

def clear(path):
    consent = input("Are you sure you want to clear your todolist?\n([y]es or [n]o) "+promptcol+prompt+END)
    if (consent == "y" or consent == "Y" or consent == "yes" or consent == "Yes" or consent == "YES"):
        file = open(path, "w")
        file.write("")
        file.close()

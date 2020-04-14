import os
from config import *
from os.path import expanduser, isfile

# path to name_of_todolist.todolist (defined in config.py)
path = os.path.expanduser(notes_path)

# load todolist to python list
def load(path):
    list = []
    file = open(path, 'r')
    lines = file.readlines()
    for i in range(len(lines)):
        note, state = (lines[i].rstrip("\n")).split("|")
        list.append([note, state])
    return list

# print todolist from python list
def show(todo):
    print("\033c", end="")
    if(showtitle == True):
        print(title)
    for i in range(len(todo)):
        if(todo[i][1] == "0"):
            print(unfinished+" "+todo[i][0])
        if(todo[i][1] == "1"):
            print(finished+" "+todo[i][0])
    print(" ")

# save changes to todolist file
def save(todo, path):
    file = open(path, 'w')
    file.write("")
    file.close()
    file = open(path, 'a')
    for i in range(len(todo)):
        file.write(todo[i][0]+"|"+todo[i][1]+"\n")

# add '1' flag (done) to a task
def check(todo, n):
    try:
        tasknum = int(n) - 1
    except:
        tasknum = len(todo) + 1
    try:
        todo[tasknum][1] = "1"
    except:
        pass

# add '0' flag (not done) to a task
def uncheck(todo, n):
    try:
        tasknum = int(n) - 1
    except:
        tasknum = len(todo) + 1
    try:
        todo[tasknum][1] = "0"
    except:
        pass

# create new task (in todolist python list)
def new(todo, note):
    todo.append([note, "0"])

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
    consent = input("Are you sure yu want to clear your todolist?\n([y]es or [n]o) "+prompt)
    if (consent == "y" or consent == "Y" or consent == "yes"):
        file = open(path, "w")
        file.write("")
        file.close()

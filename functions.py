import os
from config import *
from os.path import expanduser, isfile
from datetime import datetime

# TODO: task descriptions

# todolist structure: [[task text, flag, duedate], [task text, flag, duedate]]

# fetch current date
todate = datetime.today()

# change flag of task | args: (todolist, flag command, number of task)
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

# load todolist | args: (path to todolist) | returns: todolist, todolist title
def load(path):
    todo = []
    file = open(path, 'r+')
    pretitle, mess = str(os.path.basename(file.name)).split(".")
    title = pretitle+": "
    lines = file.readlines()
    for i in range(len(lines)):
        try:
            task, flag, duedate = (lines[i].rstrip("\n")).split("|")
            due = datetime.strptime(duedate, '%Y-%m-%d')
            todo.append([task, flag, due])
        except:
            task, flag  = (lines[i].rstrip("\n")).split("|")
            todo.append([task, flag, "none"])
    return todo, title

# render todolist | args: (todolist, todolist title)
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
                taskinfo = flags[y][1][0] + " " + todo[i][0]
                if(showdeadline == False):
                    if(type(todo[i][2]) is datetime):
                        if(todo[i][2] >= todate):
                            print(flags[y][2][0] + taskinfo + END)
                        elif(todo[i][2] < todate and flags[y][2][1] == True):
                            print(flags[y][2][0] + taskinfo + END)
                        else:
                            print(RED + taskinfo + END)
                    else:
                        print(flags[y][2][0] + taskinfo + END)
                if(showdeadline == True):
                    if(type(todo[i][2]) is datetime):
                        if(todo[i][2] >= todate):
                            print(flags[y][2][0] + taskinfo + END + " " + " → " + todo[i][2].strftime(dateformat))
                        elif(todo[i][2] < todate and flags[y][2][1] == True):
                            print(flags[y][2][0] + taskinfo + END + " " + " → " + todo[i][2].strftime(dateformat))
                        else:
                            print(RED + taskinfo + END + " " + " → " + todo[i][2].strftime(dateformat))
                    else:
                        print(flags[y][2][0] + taskinfo + END)
                break
    print(" ")

# save todolist | args: (todolist, path to todolist file)
def save(todo, path):
    file = open(path, 'w')
    file.write("")
    file.close()
    file = open(path, 'a')
    for i in range(len(todo)):
        if(type(todo[i][2]) is datetime):
            file.write(todo[i][0] + "|" + todo[i][1] + "|" + todo[i][2].strftime('%Y-%m-%d') + "\n")
        else:
            file.write(todo[i][0] + "|" + todo[i][1] + "\n")

# create new task | args: (todolist, text)
def new(todo, task):
    todo.append([task, deflag, "none"])

# change duedate of task | args: (todolist, number of task)
def change_date(todo, n):
        try:
            tasknum = int(n) - 1
        except:
            tasknum = len(todo) + 1

        if(thisyear == False):
            duedate = input("(Year month day) " + promptcol + prompt + END)
        else:
            duedate = input("(month day) " + promptcol + prompt + END)
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

# remove single task | args: (todolist, number of task)
def remove(todo, n):
        try:
            tasknum = int(n) - 1
        except:
            tasknum = len(todo) + 1
        try:
            todo.pop(tasknum)
        except:
            pass

# remove all tasks | args: (todolist)
def clear(todo):
    consent = input("Are you sure you want to clear your todolist?\n([y]es or [n]o) " + promptcol + prompt + END)
    consent.lower()
    if(consent == "y" or consent == "yes"):
        todo.clear()

# sort todolist | args: (todolist, sorting method, sort direction)
# sort_type: date/d, priority/p
# direction: highest/h, lowest/l
def sort_by(todo, sort_type, direction):
    sort_type.lower()
    direction.lower()

    # sort todolist by duedates assigned to tasks
    if(sort_type == "date" or sort_type == "d"):
        wdate = []
        wodate = []
        for i in range(len(todo)):
            if(todo[i][2] != "none"):
                wdate.append(todo[i])
            else:
                wodate.append(todo[i])
        todo.clear()
        if(direction == "h" or direction == "highest"):
            wdate.sort(key=lambda date: date[2], reverse=True)
        if(direction == "l" or direction == "lowest"):
            wdate.sort(key=lambda date: date[2])
        for i in range(len(wdate)):
            todo.append(wdate[i])
        for i in range(len(wodate)):
            todo.append(wodate[i])
    
    # sort todolist by priority value of flags assigned to tasks
    if(sort_type == "priority" or sort_type == "p"):
        wpriority = []
        for i in range(len(todo)):
            for y in range(len(flags)):
                if(todo[i][1] == flags[y][1][1]):
                    wpriority.append(todo[i] + [flags[y][3]])
                    print(wpriority[i])
        if(direction == "h" or direction == "highest"):
            wpriority.sort(key=lambda p_index: p_index[3], reverse=True)
        elif(direction == "l" or direction == "lowest"):
            wpriority.sort(key=lambda p_index: p_index[3])
        todo.clear()
        for i in range(len(wpriority)):
            todo.append([wpriority[i][0], wpriority[i][1], wpriority[i][2]])

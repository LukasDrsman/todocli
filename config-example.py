# change name from config-example.py to config.py

# colour codes
BLACK  = '\33[30m'
RED    = '\33[31m'
GREEN  = '\33[32m'
YELLOW = '\33[33m'
BLUE   = '\33[34m'
VIOLET = '\33[35m'
BEIGE  = '\33[36m'
WHITE  = '\33[37m'
GREY   = '\33[90m'
NONE   = ''
END    = '\033[0m'

# task state visualizers (flags)
# syntax: (("command-short", "command"), ("symbol", "code"), (colour-name, overwrite-deadline-colour))
flags = [
        (("i", "important"), ("●", "2"), (YELLOW, False)),
        (("uc", "uncheck"), ("□", "0"), (NONE, False)),
        (("cc", "check"), ("■", "1"), (GREY, True))
        ]

# default flag on creation of task
deflag = "0"

# default path to default todolist
defpath = "~/todocli/todo.todolist"

# path to folder containing todolists
defdir = "~/todocli/"

# list all todolist files when selecting todolist file
listtodos = True

# title of todo-list
showtitle = True

# show deadline of task
showdeadline = True

# prompt
prompt = "▶ "
promptcol = GREEN

# save changes on exit
writeonexit = True

# deadline date format
dateformat = "%a %d %b"

# use this year
thisyear = False

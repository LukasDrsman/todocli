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

# task state visualizers (flags)
# syntax: (("command-short", "command"), ("symbol", "code"), (colour-name, overwrite-deadline-colour))
flags = [
        (("i", "important"), ("●", "2"), (YELLOW, False)),
        (("uc", "uncheck"), ("□", "0"), (NONE, False)),
        (("cc", "check"), ("■", "1"), (GREY, True))
        ]

# default flag on creation of task
deflag = "0"

# path to notes file
npath = "~/todocli/notes.todolist"

# title of todo-list
showtitle = True
title = "TODO"

# show deadline of task
showdeadline = True

# prompt
prompt = "▶ "
promptcol = GREEN

# save changes on exit
writeonexit = True

# deadline date format
dateformat = "%a %d %b"

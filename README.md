# todocli
Simple, CLI based TODO list, written in python.<br/>
<br/>
## How to run and use
To run this, you need: python3 os, os.path, sys, bash, linux or macOS (wasn't tested on macOS) <br/> <br/>
Download and run (using terminal, in home dir): 
```
git clone https://github.com/LukyIsHere/todocli
cd todocli
python3 main.py
```
<br/>
Commands:<br/>
 help / h  - shows manual <br/>
 new / n  - adds new TODO line<br/>
 read / r  - prints all TODO lines<br/>
 show / s  - clears screen and prints all TODO lines<br/>
 delete / del  - clears TODO list<br/>
 uncheck / uc  - unchecks TODO line<br/>
 check / cc  - checks TODO line<br/>
 quit / q  - exits program<br/>
<br>

## Configuration of todocli

Written in python.<br/><br/>
Configurable presets ('config.py'):
```
unfinished = "insert_unchecked_symbol_here"
finished = "insert_checked_symbol_here"
notes_path = "insert_notes_path_here"
hlp_path = "insert_help_path_here"
title = "insert_title_of_TODOlist_here"
```
<br/>

## Things to be done
* single-line deletion
* further configuration options
* more efficient code
* cleaner code
* marking options for sepcial items


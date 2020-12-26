This repo is old and unreliable, use ![this one instead](https://github.com/LukasDrsman/tdmcli)
# todocli
![preview](https://github.com/LukasDrsman/todocli/blob/master/preview.png)
<br/>
## Installation
#### Requirements:
* python3

#### Install and run:
```sh
git clone https://github.com/LukasDrsman/todocli.git
cd todocli
# edit and rename config-example.py to config.py
sudo ./install
todocli
```
## Usage
```
▶ [short or long] [arguments] 
```
| long        | short           | description  | arguments |
| ------------- |:-------------:| -----|-----------:|
|new       |n       |creates new task         |text| |
|clear     |cl      |clears todolist          | | |
|remove    |rm      |removes task             |task number| |
|load      |l       |loads different todolist | |
|write     |w       |saves todolist           | |
|quit      |q       |exits program            | |
|exit      |x       |exits program            | |
|uncheck   |uc      |marks task as not done   |task number|
|check     |cc      |marks task as done       |task number|
|date      |d       |sets deadline            |task number|
|important |i       |marks task as important  |task number|
|sort      |s       |sorts todolist           |sorting parameters|

#### Sorting:
```
▶ s [sort by] [order] 
```
| sort by (long)| sort by (short) | description  |
| ------------- |:---------------:| -------------:|
|date           |d                |sorts by tasks assigned deadline   |
|priority       |p                |sorts by priority index of tasks' flags  |

| order (long)        | order (short)           | description  |
| ------------- |:-------------:| ----------------:|
|highest       |h       |descending order       |
|lowest        |l       |ascending order        |

<br>

# todol

Simple and minimalistic to-do list tracker in python. Everything is saved in text-file on your local drive. Sync among devices can be achieved with ownCloud/Google Drive/Dropbox. 

Name files "_tdl.md" for automatic checkbox addition. 

## Features 

- `-add [text]` - add new item to to-do list
- `-insert [id] [text]` - insert new item in position of `id` to-do list
- `-done [id] [id] ...` - checkout item as done
- `-undone [id] [id] ...` - uncheckout item
- `-edit [id] [id] ...` - edit todos
- `-all` - print all todos (done/undone) 
- `-clear` - clears all to-dos
- `-backup` - creates backup in separate folder backup
- `-switch [name]` - switch to different to-do list or create new todo list
- `..` - return to default todolist

For shorthand, you can use just first letter `-a`,`-d`, `-e`, etc.

Example 

```
pc@usr:$ tdl
----------------------
file: todo_tdl.md | ['other_list_tdl.md', 'todo_tdl.md']
----------------------
(0)  [ ] github.com
(1)  [ ] task 2
(2)  [ ] task 1
----------------------
```


## Install 

```
cd $path
git clone https://github.com/jy-r/todol.git
```

`~/.bashrc`

```
alias todol='python3 $path/todol/todol.py'
```





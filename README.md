# todol

To-do list in python. Simple and minimalistic to-do tracking. Everything is saved in text-file on your local drive. Sync can be done with ownCloud/Google Drive/Dropbox. 

## Features 

- `-add [text]` - add new item to to-do list
- `-done [id] [id]` - checkout item as done
- `-undone [id] [id]` - uncheckout item
- `-edit [id] [id]` - edite todos
- `-clear` - clears all to-dos
- `-backup` - creates backup 
- `-switch [name]` - swich to different to-do list


## Install 

```
cd $path
git clone https://github.com/jy-r/todol.git
```

`~/.bashrc`

```
alias todol='python3 $path/todol/todol.py'
```

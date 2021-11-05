# Git Cheat Sheet

## Setup user name and email
global setup
```
git config --global user.name "Emma Paris"
git config --global user.email "eparis@atlassian.com"
```
local setup
```
git config user.<span></span>name
```

check git config
```
git config --list
git config -l
```

edit git config directly
```
git config --edit --global
git config --edit

```
remove elements in config
```
git config --system --unset credential.helper
```

setup shortcut
```
git config --global alias.<span></span>alias-name git-command
```

aviod enter credential each time
```
git config credential.helper store
https://stackoverflow.com/questions/11403407/git-asks-for-username-every-time-i-push
```

## git basic
```
- git commit -m "message"
- git fetch
- git pull
- git push
```

overwrite the last commit
```
git commit --amend
```

be sensitive about the file name
```
git config core.ignorecase false
```

undo the changes after git add
```
git reset .
```

## Git Add
stages new files and modifications, without `deletions` in the current directory
- git add .

stages modifications and deletions, without `new files` in the current directory
- git add -u

stages `all changes` in the current directory
- git add -A

add specific drectory or files
- git add directory/files

good explanation
https://stackoverflow.com/questions/572549/difference-between-git-add-a-and-git-add


## Git Check
check which files are staged, unstaged, and untracked.
- git status

check commit history
- git log 

## Git Checkout
Create new branch and switch to that branch
git checkout -b branch


## Remote
Create a new connection to a remote repo. After adding a remote, you can use name as a shortcut for url in other commands.
- git remote add name url

check remote fetch and push
- git remote -v

## Stash
Stash the changes in a dirty working directory away
- git stash

## Useful Alias
```
git s
- alias.s=status

git a
- alias.a=!git add . && git status

git au
- alias.au=!git add -u . && git status

git cm 'message'
- alias.cm=commit -m

git acm
- alias.acm=!git add . && git commit -m

git ca
- alias.ca=commit --amend

git d
- alias.d=diff

git lg 
- alias.lg=log --color --graph --pretty=format:'%C(bold white)%h%Creset -%C(bold green)%d%Creset %s %C(bold green)(%cr)%Creset %C(bold blue)<%an>%Creset' --abbrev-commit --date=relative
```
## Change Branch Name
```
git branch -m new-name
git push origin :old-name new-name
git push origin -u new-name
```

## Unuseful Alias 
git l
- alias.l=log --graph --all --pretty=format:'%C(yellow)%h%C(cyan)%d%Creset %s %C(white)- %an, %ar%Creset'

git ll
- alias.ll=log --stat --abbrev-commit

git llg
- alias.llg=log --color --graph --pretty=format:'%C(bold white)%H %d%Creset%n%s%n%+b%C(bold blue)%an <%ae>%Creset %C(bold green)%cr (%ci)' --abbrev-commit

- alias.c=commit
- alias.master=checkout master
- alias.ac=!git add . && git commit

## Create .gitignore
https://www.atlassian.com/git/tutorials/saving-changes/gitignore


## Git Step by Step
- All steps
https://stackoverflow.com/questions/46877667/how-to-push-a-new-initial-project-to-github-using-vs-code
```
- git init
- git add README.md
- git commit -m "first commit"
- git remote add origin https://github.com/jinisaweaklearner/betfair_nba_datathon_2020.git
- git push -u origin master
```


# Git Rebase
- https://stackoverflow.com/questions/11696295/rejected-master-master-non-fast-forward
- git pull --rebase


## Git Stash
```
- git stash
- git stash list --all
- git stash clear
```

## There is no tracking information for the current branch
```
git pull origin master
```

## Clone Repo
```
- sudo apt-get install git
- sudo git init
- sudo git remote add origin https://USER@bitbucket.org/powerwrapltd/pwl-ods.git
- sudo git pull into ~/ods
```

## set up upstream of master 
```
git branch --set-upstream-to=origin/master master
```

## skip CICD
```
add [skip ci] in comments
```

## useful command
```
git log --online
git commit --amend
git rebase -i HEAD~4
```

## combine commits after push
```
git checkout my_branch
git reset --soft HEAD~4
git commit
git push --force origin my_branch
```

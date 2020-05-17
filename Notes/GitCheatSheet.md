---
title: Git Cheat Sheet
created: '2020-04-10T05:59:27.884Z'
modified: '2020-04-10T08:28:29.717Z'
---

# Git Cheat Sheet

## Setup user name and email
global setup
- git config --global user.<span></span>name "Emma Paris"
- git config --global user.<span></span>email "eparis<span></span>@atlassian.com"

local setup
- git config user.<span></span>name

check git config
- git config --list

setup shortcut
- git config --global alias.<span></span>alias-name git-command

## Git Basic
- git commit -m "message"
- git fetch
- git pull
- git push

overwrite the last commit 
git commit --amend

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

## Change Branch Name

git branch -m new-name

git push origin :old-name new-name

git push origin -u new-name


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





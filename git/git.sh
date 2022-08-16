#!/usr/bin/env bash

function git-rename-last-commit() {
  git commit --ammend
}

function git-add-and-commit() {
  git add -A
  git commit -m $argv[1]
}

function git-add-commit-push() {
  validate-param "repository path" $1
  commitMessage=$1
  git add -A
  git commit -m ${commitMessage}
  git push origin master
}

function git-branches-info() {
  git for-each-ref --sort=committerdate refs/heads/ --format='%(HEAD) %(color:yellow)%(refname:short)%(color:reset) - %(color:red)%(objectname:short)%(color:reset) - %(contents:subject) - %(authorname) (%(color:green)%(committerdate:relative)%(color:reset))'
}

function git-init-submodules() {
  git submodule update --init --recursive
}

function git-clone-with-submodules() {
  validate-param "repository path" $1
  git clone --recursive -j8 $1
}

function git-fix-upstream() {
  validate-param "upstream branch" $1
  branchName=$1
  git branch --set-upstream-to=origin/${branchName} ${branchName}
}

function git-commit-hash() {
  git rev-parse --short HEAD
}

function git-branch() {
  for k in $(git branch | sed s/^..//); do echo -e $(git log -1 --pretty=format:"%Cgreen%ci %Cblue%cr%Creset" $k --)\\t"$k"; done | sort
}

# https://stackoverflow.com/questions/2928584/how-to-grep-search-committed-code-in-the-git-history
function git-search-all-branches() {
  validate-param "search query" $1
  git grep ${branchName} $(git rev-list --all)
}

function git-log() {
  git log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit
}

function git-current-branch-name() {
  git rev-parse --symbolic-full-name --abbrev-ref HEAD
}

function git-squash() {
  validate-param "commits to be squashed" $1
  git reset --soft HEAD~${1}
}

function git-undo-last-commit() {
  git reset --soft HEAD~1
}

function git-undo-commits() {
  validate-param "amount of undo commits" $1
  git reset --soft HEAD~${1}
}

function git-show-merges() {
  git log --show-pulls
}

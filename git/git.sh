#!/usr/bin/env bash

function git-log {
	git log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit
}

function git-rename-last-commit {
    git commit --ammend
}

function git-add-and-commit {
	git add -A; git commit -m $argv[1]
}

function git-branches-info {
	git for-each-ref --sort=committerdate refs/heads/ --format='%(HEAD) %(color:yellow)%(refname:short)%(color:reset) - %(color:red)%(objectname:short)%(color:reset) - %(contents:subject) - %(authorname) (%(color:green)%(committerdate:relative)%(color:reset))'
}

function git-init-submodules {
    git submodule update --init --recursive
}

function git-clone-with-submodules {
    validate-param "repository path" $1
    git clone --recursive -j8 $1
}

function git-fix-upstream {
    validate-param "upstream branch" $1
    branchName=$1
    git branch --set-upstream-to=origin/${branchName} ${branchName}
}

function git-commit-hash {
    git rev-parse --short HEAD
}
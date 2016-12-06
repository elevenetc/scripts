#!/usr/bin/env bash

function git-lg {
	git log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit
}

function git-ac {
	git add -A; git commit -m $argv[1]
}

function git-branch {
	git for-each-ref --sort=committerdate refs/heads/ --format='%(HEAD) %(color:yellow)%(refname:short)%(color:reset) - %(color:red)%(objectname:short)%(color:reset) - %(contents:subject) - %(authorname) (%(color:green)%(committerdate:relative)%(color:reset))'
}

function git-init-submodules {
    git submodule update --init --recursive
}

function git-clone-with-submodules {
    validate-param "repository path" $1
    git clone --recursive -j8 $1
}
#!/usr/bin/env python

import subprocess

if __name__ == '__main__':
    subprocess.call(
        "git log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit",
        shell=True)

#!/usr/bin/env python

import subprocess

version = '1.0'

subprocess.call(
    "git log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit",
    shell=True)

#! /usr/bin/python
import subprocess as sb
import os

sb.Popen(['pwd'], shell=True)

branches_result = sb.Popen(['git', 'branch', '-a'], stdout=sb.PIPE)
branches = branches_result.stdout.readlines()

if branches_result.poll() != 0:
    print ('error with branch')
    exit()

fetch_result = os.system('git fetch --all')

if fetch_result != 0:
    print ('error with fetch', fetch_result)
    exit()


def is_valid_name(branch_name):
    if branch_name.find('*') != -1:
        return False

    if branch_name.find('HEAD') != -1:
        return False

    if branch_name.find('remotes/origin/') != 0:
        return False

    return True


for branch in branches:

    branch = branch.strip()

    if not is_valid_name(branch):
        continue

    branch = branch.replace('remotes/origin/', '')

    print ('=====================================================: ' + branch)

    if 0 != os.system('git checkout ' + branch):
        print ('error')
        exit()

    if 0 != os.system('git merge origin/' + branch):
        print ('error')
        exit()

#! /usr/bin/python
import subprocess as sb
import os

sb.Popen(['pwd'], shell=True)

branchListResult = sb.Popen(['git', 'branch', '-a'], stdout=sb.PIPE)
branches = branchListResult.stdout.readlines()

if branchListResult.poll() != 0:
    print 'error with branch'
    exit()

ret = os.system('git fetch --all')

if ret != 0:
    print 'error with fetch', ret
    exit()

for branch in branches:

    branch = branch.strip()

    if branch.find('*') != -1:
        continue

    if branch.find('HEAD') != -1:
        continue

    if branch.find('remotes/origin/') != 0:
        continue

    branch = branch.replace("remotes/origin/", "")

    cmdCheckout = 'git checkout ' + branch
    print '=====================================================: ' + branch

    if 0 != os.system(cmdCheckout):
        print 'error'
        exit()

    cmdMerge = 'git merge origin/' + branch

    if 0 != os.system(cmdMerge):
        print 'error'
        exit()

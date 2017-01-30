import os
import re
import subprocess as sb

import general_utils


def get_last_commit_sha(branch):
    hash = sb.Popen(('git log -n 1 --pretty=format:"%H"').split(), stdout=sb.PIPE)
    lines = hash.stdout.readlines()[0]
    return lines.replace('"', '')


def current_branch_name():
    branch_cmd = sb.Popen('git rev-parse --abbrev-ref HEAD'.split(), stdout=sb.PIPE)
    return branch_cmd.stdout.readlines()[0].replace('\n', '')


def checkout_all_remote_branches():
    result = []
    branches_result = sb.Popen(['git', 'branch', '-a'], stdout=sb.PIPE)
    branches = branches_result.stdout.readlines()

    if branches_result.poll() != 0:
        print ('error with branch')
        return result

    fetch_result = os.system('git fetch --all')

    if fetch_result != 0:
        print ('error with fetch', fetch_result)
        return result

    for branch in branches:

        branch = branch.strip()

        if not general_utils.is_valid_name(branch):
            continue

        branch = branch.replace('remotes/origin/', '')
        result.append(branch)

        if 0 != os.system('git checkout ' + branch):
            print ('error')
            exit()

        if 0 != os.system('git merge origin/' + branch):
            print ('error')
            exit()

    return result


def get_ordered_map_of_commits(amount_commits):
    result = []
    cmd = 'git log -n ' + str(amount_commits) + ' --pretty=format:"%H:%s"'
    commits = sb.Popen(cmd.split(), stdout=sb.PIPE).stdout.readlines()
    for commit in commits:
        commit = commit.replace('"', '')
        sha = re.search('(.*)(?=:)', commit).group(0)
        message = re.search('(?<=:)(.*)', commit).group(0)
        result.append({'sha': sha, 'message': message})
    result.reverse()
    return result

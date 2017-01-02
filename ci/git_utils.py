import subprocess as sb
import general_utils
import os


def get_last_commit_hash(branch):
    hash = sb.Popen(('git log -n 1 ' + branch + ' --pretty=format:"%H"').split(), stdout=sb.PIPE)
    return hash.stdout.readlines()[0].replace('"', '')


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
import json
import os
import subprocess as sb
from argparse import Namespace

import requests


def load_versions(app_id, hockey_token):
    url = 'https://rink.hockeyapp.net/api/2/apps/' + app_id + '/app_versions'
    headers = {'X-HockeyAppToken': hockey_token}
    response = requests.get(url, headers=headers)
    return response.content


def load_apps(hockey_token):
    url = 'https://rink.hockeyapp.net/api/2/apps'
    headers = {'X-HockeyAppToken': hockey_token}
    response = requests.get(url, headers=headers)
    return json.loads(response.content, object_hook=lambda d: Namespace(**d)).apps


def filter_apps(apps, app_name):
    result = []
    for app in apps:
        if app.platform == 'Android' and str(app.title).startswith(app_name):
            result.append(app)
    return result


def current_branch_name():
    branch_cmd = sb.Popen('git rev-parse --abbrev-ref HEAD'.split(), stdout=sb.PIPE)
    return branch_cmd.stdout.readlines()[0].replace('\n', '')


def is_valid_name(branch_name):
    if branch_name.find('*') != -1:
        return False

    if branch_name.find('HEAD') != -1:
        return False

    if branch_name.find('remotes/origin/') != 0:
        return False

    return True


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

        if not is_valid_name(branch):
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


def filter_not_created_apps(app_name, apps, all_branches):
    result = []
    i = len(all_branches)

    while i >= 0:
        i -= 1
        branch = all_branches[len(all_branches) - 1]

        print 'check branch:' + branch

        if branch.find('feature') == -1:
            print 'invalid branch: ' + branch
            all_branches.remove(branch)
            continue

        for app in apps:

            app_title = str(app.title)

            if app_title.startswith(app_name + '-' + branch):
                print 'already created:' + branch
                all_branches.remove(branch)

    return result

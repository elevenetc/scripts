import json
import os
import subprocess as sb
from argparse import Namespace

import requests

# master
# release/0.0.0
# feature/APP-000-name
# fix/APP-000-name
prefixes = ['production', 'release', 'feature', 'fix']


def load_all_apps(hockey_token):
    url = 'https://rink.hockeyapp.net/api/2/apps'
    headers = {'X-HockeyAppToken': hockey_token}
    response = requests.get(url, headers=headers)
    return json.loads(response.content, object_hook=lambda d: Namespace(**d)).apps


def filter_android_apps_by_name(apps, app_name):
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


# created app should have titles:
# "Hello - production"
# "Hello - release/v1.1"
# "Hello - feature/JIRA-222-description"
# "Hello - fix/JIRA-222-description"
def filter_not_created_apps(app_name, apps, all_branches):
    result = []
    i = len(all_branches) - 1

    while i >= 0:

        branch = all_branches[i]
        i -= 1

        for prefix in prefixes:
            # check if branch has proper prefix
            if branch.find(prefix) == 0:
                # check if app created for this branch
                created = False
                for app in apps:
                    if app.title == get_title(app_name, branch):
                        created = True
                        break

                if not created:
                    result.append(branch)

    return result


def create_app(app_name, branch, hockey_token):
    url = 'https://rink.hockeyapp.net/api/2/apps/new'
    params = {
        'title': get_title(app_name, branch),
        'bundle_identifier': app_name,
        'platform': 'Android',
        'release_type': 1
    }
    headers = {'X-HockeyAppToken': hockey_token}
    response = requests.get(url, headers=headers, params=params)
    return json.loads(response.content, object_hook=lambda d: Namespace(**d))


def load_versions(app, hockey_token):
    pub_id = app.public_identifier
    url = 'https://rink.hockeyapp.net/api/2/apps/' + pub_id + '/app_versions'
    headers = {'X-HockeyAppToken': hockey_token}
    response = requests.get(url, headers=headers)
    return json.loads(response.content, object_hook=lambda d: Namespace(**d)).app_versions


def load_or_create_app(app_name, branch, hockey_token):
    apps = load_all_apps(hockey_token)
    apps = filter_android_apps_by_name(apps, app_name)
    app = is_app_created(app_name, branch, apps)

    if app is None:
        app = create_app(app_name, branch, hockey_token)

    return app


def assemble(build_type):
    branch_cmd = sb.Popen(('./gradlew assemble' + build_type.capitalize()).split(), stdout=sb.PIPE)
    return branch_cmd.stdout.readlines()


def is_app_created(app_name, branch, apps):
    for app in apps:
        if app.title == get_title(app_name, branch):
            return app
    return None


def get_last_commit_hash(branch):
    hash = sb.Popen(('git log -n 1 ' + branch + ' --pretty=format:"%H"').split(), stdout=sb.PIPE)
    return hash.stdout.readlines()[0].replace('"', '')


def get_title(app_name, branch):
    return app_name + ' - ' + branch
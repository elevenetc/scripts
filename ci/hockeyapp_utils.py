import general_utils
import build_utils
import git_utils as git
import json
import re
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


def filter_branches(all_branches):
    result = []
    i = len(all_branches) - 1

    while i >= 0:

        branch = all_branches[i]
        i -= 1

        for prefix in prefixes:
            # check if branch has proper prefix
            if branch.find(prefix) == 0:
                result.append(branch)

    return result


# created app should have titles:
# "Hello - production"
# "Hello - release/v1.1"
# "Hello - feature/JIRA-222-description"
# "Hello - fix/JIRA-222-description"
def filter_not_created_apps(app_name, apps, all_branches):
    result = []

    branches = filter_branches(all_branches)

    for branch in branches:
        created = is_app_created_for_branch(app_name, apps, branch)

        if not created:
            result.append(branch)

    return result


def is_app_created_for_branch(app_name, apps, branch):
    for app in apps:
        if app.title == general_utils.get_title(app_name, branch):
            return True
    return False


def create_app(app_name, branch, hockey_token):
    url = 'https://rink.hockeyapp.net/api/2/apps/new'
    params = {
        'title': general_utils.get_title(app_name, branch),
        'bundle_identifier': app_name,
        'platform': 'Android',
        'release_type': 1
    }
    headers = {'X-HockeyAppToken': hockey_token}
    response = requests.get(url, headers=headers, params=params)
    return json.loads(response.content, object_hook=lambda d: Namespace(**d))


def load_versions(app, hockey_token):

    print '# load_versions'

    pub_id = app.public_identifier
    url = 'https://rink.hockeyapp.net/api/2/apps/' + pub_id + '/app_versions'
    headers = {'X-HockeyAppToken': hockey_token}
    response = requests.get(url, headers=headers)
    return json.loads(response.content, object_hook=lambda d: Namespace(**d)).app_versions


def load_or_create_app(app_name, branch, hockey_token):

    print '# load_or_create_app'

    apps = load_all_apps(hockey_token)
    apps = filter_android_apps_by_name(apps, app_name)
    app = general_utils.is_app_created(app_name, branch, apps)

    if app is None:
        app = create_app(app_name, branch, hockey_token)

    return app


def create_version(app, branch, hockey_token):

    url = 'https://rink.hockeyapp.net/api/2/apps/' + app.public_identifier + '/app_versions/new'
    headers = {'X-HockeyAppToken': hockey_token}
    params = {
        'bundle_version': branch
    }

    response = requests.get(url, headers=headers, params=params)
    version = json.loads(response.content, object_hook=lambda d: Namespace(**d))
    return version


def create_and_upload_version(app, branch, versions, last_commit_sha, path_to_app_file, hockey_token):

    print '# upload_version'

    new_version = create_version(app, branch, hockey_token)

    # if len(versions) > 0:


    url = 'https://rink.hockeyapp.net/api/2/apps/' + app.public_identifier + '/app_versions/upload'
    headers = {'X-HockeyAppToken': hockey_token}
    params = {
        'status': 2,
        'notify': 1,
        'notes': create_notes(versions, last_commit_sha),
        'notes_type': 0
    }
    files = {'ipa': open(path_to_app_file, 'rb')}

    response = requests.post(url, headers=headers, params=params, files=files)
    if response == 'ddd':
        print 'hello'


def upload_last_version_if_needed(app, branch, path_to_app_file, hockey_token):

    print '# upload_last_version_if_needed'

    versions = load_versions(app, hockey_token)
    last_commit_sha = git.get_last_commit_sha(branch)
    need_to_upload = True
    for version in versions:
        if last_commit_sha not in version.notes:
            need_to_upload = False
            break

    if need_to_upload:
        build_utils.assemble('release')
        create_and_upload_version(app, branch, versions, last_commit_sha, path_to_app_file, hockey_token)


# Note should look about like this
# - commit message a
# - commit message b
# sha:
def create_notes(versions, last_commit_sha):
    result = ''
    commits = git.get_ordered_map_of_commits(100)
    last_mentioned_sha = None

    commits.reverse()

    reach_last_sha = False

    for commit in commits:
        result += commit.message
        result += '\n'

        for version in versions:
            sha = find_sha_in_note(version.notes)
            if sha == commit.sha:
                reach_last_sha = True
                break

        if reach_last_sha:
            break

    result += '(sha:' + last_commit_sha + ')'

    return result


# note sample - '(sha:xxx)'
def find_sha_in_note(note):
    return re.search('(?<=(\(sha:))(.*)(?=\))', note).group(0)
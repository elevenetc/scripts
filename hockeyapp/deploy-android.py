#! /usr/bin/env python
import glob
import os.path
import sys

import requests


def upload(apk_file_path, api_token, app_id, notify=True, notes='', dsym=''):
    if not apk_file_path:
        raise Exception('Error! Build file not specified')
    if not os.path.exists(apk_file_path):
        raise Exception('Error! {} build file doesn\'t exist'.format(apk_file_path))
    if not app_id:
        raise Exception('Undefined Hockeyapp AppId')
    if not api_token:
        raise Exception('Undefined Hockeyapp ApiToken')
    if dsym and not os.path.exists(dsym):
        raise Exception('Error! {} .dsym.zip file doesn\'t exist'.format(dsym))

    log('Uploading...')

    upload_url = 'https://rink.hockeyapp.net/api/2/apps/' + app_id + '/app_versions/upload'
    params = {}
    params['dsym'] = dsym
    params['notify'] = 2 if notify else 0
    params['notes'] = notes
    files = {'ipa': open(apk_file_path, 'rb')}
    if dsym:
        files['dsym'] = open(dsym, 'rb')
    headers = {'X-HockeyAppToken': api_token}

    req = requests.post(url=upload_url, data=params, files=files, headers=headers)

    if req.status_code >= 400:
        raise Exception(
            'Failed to upload apk. Status:{} Response:{}'.format(
                str(req.status_code),
                str(req.content))
        )
    else:
        log('Uploading finished with {}:{}'.format(req.status_code, req.status_code))


def log(msg):
    print 'uploading apk: {}'.format(msg)


def resolve_apk_path(apk_dir_path):
    paths = glob.glob(apk_dir_path + '/*.apk')
    if len(paths) > 1:
        raise Exception('More than one apk at "{}" \n apks:\n{}'.format(apk_dir_path, paths))
    elif len(paths) == 0:
        raise Exception('Not found apk at "{}"'.format(apk_dir_path))
    else:
        return paths[0]


def echo_start():
    log('Start')


def echo_end():
    log('End')


def validate_param(index, name):
    if index > len(sys.argv) - 1:
        raise Exception('No defined param {} at {}'.format(name, index))
    else:
        return sys.argv[index]


def main():
    echo_start()

    try:

        app_id = validate_param(1, 'app_id(str)')
        api_token = validate_param(2, 'app_token(str)')
        apk_dir_path = validate_param(3, 'apk_dir_path(str)')
        notes = validate_param(4, 'notes(str)')
        notify = True if validate_param(5, 'notify(int:1,2)') == '1' else False

        log('init with app_id: {}'.format(app_id))
        log('init with apk_dir_path: {}'.format(apk_dir_path))
        log('init with notes: {}'.format(notes))
        log('init with notify: {}'.format(notify))

        apk_file_path = resolve_apk_path(apk_dir_path)
        upload(apk_file_path, api_token, app_id, notify, notes)
    except Exception as e:
        log(str(e))
        echo_end()
        sys.exit(1)

    echo_end()


if __name__ == '__main__':
    main()

import sys

import hockeyapp_utils as hockey

if len(sys.argv) < 5:
    print 'Error. Invalid number of params. Valid format: python sync-branch.py app_name branch token file_path'
    sys.exit(1)

app_name = sys.argv[1]
branch = sys.argv[2]
token = sys.argv[3]
file_path = sys.argv[4]

print 'len: ' + str(len(sys.argv))
print 'app name: ' + app_name
print 'branch: ' + branch
print 'token: ' + token
print 'file_path: ' + file_path

app = hockey.load_or_create_app(app_name, branch, token)
hockey.upload_last_version_if_needed(app, branch, file_path, token)

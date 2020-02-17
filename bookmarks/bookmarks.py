#! /usr/bin/env python
import os
import sys
from os.path import expanduser


class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def c(color, text):
    return color + text + colors.ENDC


def write_cmd(key, cmd):
    print 'writing ' + key + ' = ' + cmd


def write_storage(storage):
    temp_file = open(temp_file_path, 'w')
    for name in storage:
        temp_file.write(name + ' ' + storage[name])
        temp_file.write('\n')
    temp_file.close()

    os.remove(file_path)
    os.rename(temp_file_path, file_path)


def load_storage():
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    if not os.path.exists(file_path):
        open(file_path, 'w').close()

    lines = tuple(open(file_path, 'r'))

    result = {}

    for raw_bookmark in lines:
        sep_index = raw_bookmark.find(' ')
        name = raw_bookmark[0:sep_index]
        value = raw_bookmark[(sep_index + 1):(len(raw_bookmark) - 1)]
        result[name] = value

    return result


def get():
    storage = load_storage()

    for name in storage:
        print c(colors.OKGREEN, name) + ': ' + storage[name]


def put(name, cmd):
    storage = load_storage()
    storage[name] = cmd
    write_storage(storage)


def remove(name):
    storage = load_storage()
    del storage[name]
    write_storage(storage)


if __name__ == '__main__':

    sync_dir = os.getenv('SYNC_DIR', None)

    if len(sys.argv) == 1:
        print c(colors.FAIL, 'Action should be one of ') + c(colors.OKGREEN, 'get, put, remove')
    elif sync_dir is None:
        print c(colors.FAIL, 'Error: ') + c(colors.OKGREEN, 'Undefined SYNC_DIR')
    else:

        file_name = "bookmarks.txt"
        dir_name = ".bookmarks"
        dir_path = sync_dir + "/" + dir_name
        file_path = dir_path + "/" + file_name
        temp_file_path = dir_path + "/temp.txt"

        action = sys.argv[1]

        if action == 'get':
            get()
        elif action == 'put':
            name = sys.argv[2]
            cmd = sys.argv[3]
            put(name, cmd)
        elif action == 'remove':
            name = sys.argv[2]
            remove(name)
        else:
            print c(colors.FAIL, 'Undefined action "' + action + '" should be one of: ') + c(
                colors.OKGREEN, 'get, put,  remove')

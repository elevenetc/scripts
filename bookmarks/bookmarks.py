#! /usr/bin/env python
import os
import sys
from os.path import expanduser

home = expanduser("~")
file_name = "bookmarks.txt"
dir_name = ".bookmarks"
dir_path = home + "/" + dir_name
file_path = dir_path + "/" + file_name
temp_file_path = dir_path + "/temp.txt"


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
        print name + ': ' + storage[name]


def put(name, cmd):
    storage = load_storage()
    storage[name] = cmd
    write_storage(storage)


def delete(name):
    print 'delete ' + name


if __name__ == '__main__':

    action = sys.argv[1]

    if action == 'get':
        get()
    elif action == 'put':
        name = sys.argv[2]
        cmd = sys.argv[3]
        put(name, cmd)
    else:
        print 'no action "' + action + '"'

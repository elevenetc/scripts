#! /usr/bin/env python
import subprocess
import sys


def get_devices_ids():
    lines = subprocess.Popen('adb devices', shell=True, stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT).stdout.readlines()
    devices = []

    for line in lines:
        if ('device' in line) and ('devices' not in line):
            devices.append(line.replace('\tdevice', '').replace('\n', ''))

    return devices


if __name__ == '__main__':

    devices = get_devices_ids()

    if len(sys.argv) <= 1:
        raise Exception('no command passed')

    if len(devices) == 0:
        raise Exception('no connected devices')

    params = " ".join(sys.argv[1:])

    for device in devices:
        cmd = 'adb -s ' + device + ' ' + params
        print ('calling: ' + cmd)
        lines = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
                                 stderr=subprocess.STDOUT).stdout.readlines()

        tab = '\t'

        for line in lines:
            line = line.replace('\n', '')
            if len(line) > 0:
                print (tab + line)

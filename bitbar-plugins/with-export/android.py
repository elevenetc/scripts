#!/usr/bin/env -S PATH="${PATH}:/usr/local/bin" python3
# coding=utf-8

import subprocess

result = subprocess.run(['adb', 'devices'], stdout=subprocess.PIPE)

lines = str(result.stdout).split('\\n')
devices_count = 0
devices = []

for line in lines:
    if 'tdevice' in line:
        devices.append(line.replace('\\tdevice', ''))
        devices_count += 1

print("📱:" + str(devices_count))

if devices_count > 0:
    print('---')

    for device in devices:
        print(device)
        print('--Reboot|terminal=false refresh=true bash="adb -s ' + device + ' reboot"')
        print('--Shutdown')

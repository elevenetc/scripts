#!/usr/bin/env -S PATH="${PATH}:/usr/local/bin" python3

import subprocess

result = subprocess.run(['adb', 'devices'], stdout=subprocess.PIPE)

lines = str(result.stdout).split('\\n')
devices_count = 0
devices = []

for line in lines:
    if 'tdevice' in line:
        devices.append(line.replace('\\tdevice', ''))
        devices_count += 1

print('adb:' + str(devices_count))

if devices_count > 0:
    print('---')

    for device in devices:
        print(device)
        print('--Reboot|terminal=false refresh=true bash=adb param1=-s param2=' + device + ' param3=reboot')
        print('--Shutdown')

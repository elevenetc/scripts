#!/usr/bin/env -S PATH="${PATH}:/usr/local/bin" python3
# coding=utf-8

import re
import subprocess

count = 10
time_pattern = re.compile('time=\d+.\d+')

result = subprocess.run(['ping', '-c', str(count), 'google.com'], stdout=subprocess.PIPE)
raw_times = time_pattern.findall(str(result.stdout))
times = []

for t in raw_times:
    time = float(t.split('=')[1])
    times.append(time)

times.sort()

if len(times) == 0:
    print("📡: no")
else:
    total = 0
    for t in times:
        total += t

    average = total / count

    print("📡: " + str(int(average)) + 'ms')
    print("---")
    for t in times:
        print (str(t))

#!/usr/bin/env -S PATH="${PATH}:/usr/local/bin" python3
# coding=utf-8


import psutil

# print("cpu:" + str(psutil.cpu_percent()))
# print(psutil.cpu_times())
# print(psutil.cpu_stats())
# print(psutil.cpu_times_percent())
# print(psutil.cpu_count())
# print(psutil.cpu_freq())
#
# print ('\n')

count = psutil.cpu_count()
samples = 3


def get_perc(f):
    f /= 10
    result = ''
    for i in range(count):
        if i < f:
            result += '■'
        else:
            result += '□'

    return result


def get_cpu_usage():
    result = []
    for x in range(samples):
        result.append(psutil.cpu_percent(interval=1, percpu=True))
    return result


usage = get_cpu_usage()
average_cpus = []
average = 0

for n in range(count):
    average_cpus.append(0)

for group in usage:
    i = 0
    for cpu in group:
        average_cpus[i] += cpu
        i = i + 1

average_cpus.sort()

for i in range(count):
    average_cpus[i] = average_cpus[i] / samples

for a in average_cpus:
    average += a

average /= count

print("cpu:" + str(int(average)))
print("---")
for a in average_cpus:
    print (get_perc(a))

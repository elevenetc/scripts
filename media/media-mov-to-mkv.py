#!/usr/bin/env python

import subprocess
import sys

version = '1.0'

print '\nStart: ' + version + '\n'

params = sys.argv[1:]

if len(params) == 0:
    print 'No params'
else:
    for i, fileName in enumerate(params):
        name = fileName.split('.')[0]

        arguments = [
            '-y', '-i',
            name + '.mov',
            '-r', '30',
            # '-s', '1280:720',
            '-s', '854:480',
            '-c:v', 'libx264',
            '-preset', 'medium',
            '-profile:v', 'baseline',
            '-level', '3.0',
            '-b:v', '256k',
            '-filter:v', 'hqdn3d=4:4:6:6',
            '-pass', '1',
            '-an',
            '-f', 'matroska',
            name + '.mkv'
        ]

        command = ['ffmpeg']
        command.extend(arguments)
        output = subprocess.Popen(command, stdout=subprocess.PIPE).communicate()[0]

print '\nFinish\n'

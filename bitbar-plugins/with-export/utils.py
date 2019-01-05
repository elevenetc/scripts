#!/usr/bin/env -S PATH="${PATH}:/usr/local/bin" python3
# coding=utf-8
import os

env_var_names = os.environ

print("🤖")
print('---')
print('env vars')

for name in env_var_names:
    print('--' + name)
    print('----copy name|terminal=true bash="echo \"' + name + '\" \| pbcopy"')
    print('----copy name|terminal=false bash=echo param1=' + name + ' param2=| param3=pbcopy')
    print('----copy value')
    print('----copy both')

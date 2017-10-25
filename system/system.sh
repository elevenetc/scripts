#!/usr/bin/env bash

function system-edit-env-gui {
    #seem more: https://stackoverflow.com/a/4567308/798165
    sudo nano /etc/launchd.conf
}

function system-edit-env-shell {
    sudo nano ~/.bash_profile
}

function system-set-env-gui {
    validate-param "env name" $1
    validate-param "env value" $2
    sudo launchctl setenv ${1} ${2}
}
#!/usr/bin/env bash

function and-adb-screen-pull {
	adb shell screencap -p /sdcard/temp.png
	adb pull /sdcard/temp.png ~/
	adb shell rm /sdcard/temp.png
	finish-with-success
}

function and-adb-restart {
    adb kill-server; adb start-server
}

function and-adb-uninstall-app {
    validate-param "package name" $1
    adb shell pm uninstall ${1}
}

function and-is-app-installed {
    validate-param "package name" $1
    if [ -z $(adb shell pm list packages | grep ${1}) ]; then
        green-prefix-message "${1}" " is not installed"
    else
        green-prefix-message "${1}" " is installed"
    fi
}
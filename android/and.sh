#!/usr/bin/env bash

function and-adb-screen-pull {

    dir=~/android-screenshots/
    name=$(date).png
    name=${name// /_}

    mkdir -p ${dir}
	adb shell screencap -p /sdcard/${name}
	adb pull /sdcard/${name} ${dir}
	adb shell rm /sdcard/${name}
	echo ${dir}${name}
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

function and-sys-version {
    adb shell getprop ro.build.version.release
}

function and-kill-app {
    validate-param "package name" $1
    adb shell am force-stop ${1}
}

function and-get-android-id {
    adb shell content query --uri content://settings/secure --where "name=\'android_id\'"
}

function and-delete-android-id {
    adb shell content delete --uri content://settings/secure --where "name=\'android_id\'"
}

function and-set-android-id {
    validate-param "AndroidID" $1
    adb shell content insert --uri content://settings/secure --bind name:s:android_id --bind value:s:${1}
}

function adb-pull-prefs {
    validate-param "package name" $1
    validate-param "prefs xml file name" $2
    adb exec-out run-as ${1} cat /data/data/${1}/shared_prefs/${2}.xml
}
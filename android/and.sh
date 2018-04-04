#!/usr/bin/env bash

function adb-adb-screen-pull {

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

function adb-adb-restart {
    adb kill-server; adb start-server
}

function adb-adb-uninstall-app {
    validate-param "package name" $1
    adb shell pm uninstall ${1}
}

function adb-is-app-installed {
    validate-param "package name" $1
    if [ -z $(adb shell pm list packages | grep ${1}) ]; then
        green-prefix-message "${1}" " is not installed"
    else
        green-prefix-message "${1}" " is installed"
    fi
}

function adb-sys-version {
    adb shell getprop ro.build.version.release
}

function adb-kill-app {
    validate-param "package name" $1
    adb shell am force-stop ${1}
}

function adb-get-android-id {
    adb shell content query --uri content://settings/secure --where "name=\'android_id\'"
}

function adb-delete-android-id {
    adb shell content delete --uri content://settings/secure --where "name=\'android_id\'"
}

function adb-set-android-id {
    validate-param "AndroidID" $1
    adb shell content insert --uri content://settings/secure --bind name:s:android_id --bind value:s:${1}
}

function adb-pull-prefs {
    validate-param "package name" $1
    validate-param "prefs xml file name" $2
    adb exec-out run-as ${1} cat /data/data/${1}/shared_prefs/${2}.xml
}

function adb-input-text {
    validate-param "text to input" $1
    adb exec-out input text $1
}

function adb-input-tap {
    validate-param "x location" $1
    validate-param "y location" $2
    adb exec-out input tap $1 $2
}

function adb-pull-screen-xml {
    adb shell uiautomator dump
    adb pull /sdcard/window_dump.xml
    adb shell rm /sdcard/window_dump.xml
    tidy -xml -i window_dump.xml > screen-layout.xml
    rm window_dump.xml
    open screen-layout.xml
}
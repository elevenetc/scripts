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

function adb-packages {
    adb shell 'pm list packages -f' | sed -e 's/.*=//' | sort
}

function adb-ip {
    adb shell ip route | awk '{print $9}'
}

function adb-connect-to-wifi {
    ip="$(adb shell ip route | awk '{print $9}')"
    port=5555
    adb tcpip ${port}
    adb connect ${ip}:${port}
}

function android-target-sdk-version {
    aapt list -a $1 | grep targetSdkVersion | grep -o '....$' | awk '{print $1+0}'
}

function android-open-apk-dir {
    find . -name "apk" | xargs open
}

function android-sdk-list-of-available-tools {
    sdkmanager --list
}

function android-sdk-install {
    validate-param "tool to install" $1
    sdkmanager $1
}

function android-sdk-update {
    android update sdk --no-ui --all
}

function android-sdk-avds-created {
    avdmanager list avd
}

function android-sdk-avds-available {
    avdmanager list
}

function android-sdk-create-avd {
    validate-param "name (without spaces)" $1
    validate-param "package (see android-sdk-list-of-available-tools)" $2
    validate-param "device id (like 10, see android-sdk-avds-available)" $3

    avdmanager create avd --name "{$1}" --package "{$2}" --device $3
}

function android-sdk-run-emulator {
    validate-param "emulator name" $1
    emulator -avd $1
}

function android-sdk-delete-avd {
    validate-param "emulator name" $1
    avdmanager delete avd -n "{$1}"
}

function android-kill-avd {
    validate-param "device name, like emulator-5554" $1
    adb -s $1 emu kill
}
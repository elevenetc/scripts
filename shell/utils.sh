#!/usr/bin/env bash

function kill-by-port {
	lsof -P | grep ':$argv[1]' | awk '{print $2}' | xargs kill
}

function get-ip {
	ifconfig | grep "inet " | grep -v 127.0.0.1 | awk '{print $2}' 
}

function get-ports {
	sudo lsof -i -P | grep -i "listen"
}

function find-text {
	grep -r ${argv}[1] ./
}

function get-app-by-port {
	lsof -i :${argv}[1]
}

function adb-screen-pull {
	adb shell screencap -p /sdcard/temp.png
	adb pull /sdcard/temp.png ~/
	adb shell rm /sdcard/temp.png
	echo 'File saved in ~/temp.png'
}
#!/usr/bin/env bash

function net-get-public-ip {
    curl http://icanhazip.com
}

function net-get-ports {
	sudo lsof -i -P | grep -i "listen"
}

function net-kill-by-port {
	lsof -P | grep ':$argv[1]' | awk '{print $2}' | xargs kill
}

function net-get-ip {
	ifconfig | grep "inet " | grep -v 127.0.0.1 | awk '{print $2}'
}

function net-get-app-by-port {
	lsof -i :$1
}

function net-check-if-port-opened {
    validate-param "host" $1
    validate-param "port" $1
    telnet $1 $2
}
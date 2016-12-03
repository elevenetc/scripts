#!/usr/bin/env bash

function pm2-log {
    validate-param "appName" $1
    pm2 logs ${1} --lines 1000
}
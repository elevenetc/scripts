#!/usr/bin/env bash

function pm2-log {
    pm2 logs ${argv} --lines 1000
}
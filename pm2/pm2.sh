#!/usr/bin/env bash

function pm2-log {
    pm2 logs ${argv}[1] --lines 1000
}
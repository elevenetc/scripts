#!/usr/bin/env bash

function ssh-copy-public-key {
    validate-param "name" $1
    validate-param "host" $2
    ssh-copy-id ${1}@${2}
}
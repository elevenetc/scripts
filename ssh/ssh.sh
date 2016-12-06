#!/usr/bin/env bash

function ssh-push-public-key {
    validate-param "name" $1
    validate-param "host" $2
    ssh-copy-id ${1}@${2}
}

function ssh-copy-public-key {
    pbcopy < ~/.ssh/id_rsa.pub
}
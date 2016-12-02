#!/usr/bin/env bash

function fs-list-by-date {
    ls -halt
}

function fs-zip-dit-with-pass {

    RED='\033[0;31m'
    NC='\033[0m'

    if [ -z "$1" ]
      then
        message-error-no-args "source dir"
        return
    fi

    srcDir=$1
    zipFile="${srcDir}.zip"
    zip -er ${zipFile} ${srcDir}
    finish-with-success
}
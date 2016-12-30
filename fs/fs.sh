#!/usr/bin/env bash

function fs-list-by-date {
    ls -halt
}

function fs-zip-dir-with-pass {

    validate-param "source dir" $1

    srcDir=$1
    zipFile="${srcDir}.zip"
    zip -er ${zipFile} ${srcDir} -x "*.DS_Store"
    finish-with-success
}

function fs-zip-dir {

    validate-param "source dir" $1

    srcDir=$1
    zipFile="${srcDir}.zip"
    zip -r ${zipFile} ${srcDir} -x "*.DS_Store"
    finish-with-success
}

function fs-find {
    validate-param "File name" $1
    find ./ -name $1
}
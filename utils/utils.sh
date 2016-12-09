#!/usr/bin/env bash

function utils-find-text {
	grep -r ${argv} ./
}

function utils-is-osx {
    if [[ "$OSTYPE" == "darwin"* ]]; then
        return 1
    else
        return 0
    fi
}

function utils-is-linux {
    if [[ "$OSTYPE" == "linux-gnu" ]]; then
        return 1
    else
        return 0
    fi
}

# Samples

#function checkOsSample {
#    utils-is-osx; isMacOS=$?
#    echo ${isMacOS}
#    if [[ "${isMacOS}" == '1' ]]; then
#        echo 'true'
#    else
#        echo 'false'
#    fi
#}
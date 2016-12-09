#!/usr/bin/env bash
function pm-update {
    utils-is-osx; isMacOS=$?
    if [[ "${isMacOS}" == '1' ]]; then
        brew update; brew upgrade
    else
        sudo apt-get update && sudo apt-get upgrade
    fi
}
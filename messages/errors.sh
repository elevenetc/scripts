#!/usr/bin/env bash

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

function validate-param {
    if [ -z "$2" ]
        then
            echo "${RED}Error:${NC} ${GREEN}$1${NC} param is undefined"
    fi
}

function message-error-no-args {
    paramName=$1
    echo "${RED}Error:${NC} no ${GREEN}${paramName}${NC} param"
}
#!/usr/bin/env bash

GREEN='\033[0;32m'
NC='\033[0m'

function finish-with-success {
    echo "${GREEN}Done.${NC}"
}

function green-prefix-message {
    echo "${GREEN}${1}${NC}${2}"
}
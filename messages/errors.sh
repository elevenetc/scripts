#!/usr/bin/env bash

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

function message-error-no-args {
    paramName=$1
    echo "${RED}Error:${NC} no ${GREEN}${paramName}${NC} param"
}
#!/usr/bin/env bash

function format-json {
    validate-param "json string like "'{"test":1,"test2":2}' $1
    echo $1 | python -mjson.tool
}

function format-json-clipboard {
    pbpaste | python -mjson.tool | pbcopy
}
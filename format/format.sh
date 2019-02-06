#!/usr/bin/env bash

function format-json {
    validate-param "json string like "'{"test":1,"test2":2}' $1
    echo $1 | python -mjson.tool
}

function format-json-clipboard {
    pbpaste | python -mjson.tool | pbcopy
    echo "${GREEN}Formatted result is in clipboard.${NC}"
}

function format-xml-clipboard() {
    pbpaste | python -c 'import sys;import xml.dom.minidom;s=sys.stdin.read();print(xml.dom.minidom.parseString(s).toprettyxml())' | pbcopy
    echo "${GREEN}Formatted result is in clipboard.${NC}"
}
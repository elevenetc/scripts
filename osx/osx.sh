#!/usr/bin/env bash

function osx-show-notification {
    title=$1
    message=$2
    params="display notification \"${title}\" with title \"${message}\""
	osascript -e ${params}
}
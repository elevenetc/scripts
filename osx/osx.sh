#!/usr/bin/env bash

function osx-show-notification {
    title=$1
    message=$2
    params="display notification \"${title}\" with title \"${message}\""
	osascript -e ${params}
}

function osx-show-hidden-files {
    defaults write com.apple.finder AppleShowAllFiles YES
    killall Finder /System/Library/CoreServices/Finder.app
}

function osx-hide-hidden-files {
    defaults write com.apple.finder AppleShowAllFiles NO
    killall Finder /System/Library/CoreServices/Finder.app
}

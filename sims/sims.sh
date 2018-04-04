#!/usr/bin/env bash

function sims-init-android-home {
    ln -s "$ANDROID_HOME/platform-tools/adb" "/usr/local/bin/adb"
}
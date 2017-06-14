#!/usr/bin/env bash

function gradle-refresh-dependencies {
    ./gradlew build --refresh-dependencies
}
#!/usr/bin/env bash

function -docker-image-shell {
    validate-param "image name" $1
    docker exec -it ${1} bash
}
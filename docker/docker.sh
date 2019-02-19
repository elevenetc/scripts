#!/usr/bin/env bash

function docker-shell {
    validate-param "image name" $1
    docker exec -it ${1} bash
}

function docker-shell-mysql {
    docker exec -it mysql bash -l
}

function docker-create-mysql {
    docker run --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=password -d mysql:latest
}


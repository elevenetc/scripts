#!/usr/bin/env bash

function mysql-login-as-root {
    mysql -u root -p
}

function mysql-login-as {
    validate-param "user name" $1
    mysql -u ${1} -p
}

function mysql-restart {
    service mysql restart
}
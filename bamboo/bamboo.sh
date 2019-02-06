#!/usr/bin/env bash

function bamboo-rest-get-plans() {
    validate-param "user name" $1
    validate-param "password" $2
    validate-param "bamboo host" $3
    curl --user {$1}:{$2} http://$3/rest/api/latest/plan?os_authType=basic
}
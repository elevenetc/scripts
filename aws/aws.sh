#!/usr/bin/env bash

function aws-get-current-user {
    aws configure list
}

function aws-get-user-policies {
    validate-param "user name"
    aws iam list-user-policies --user-name $1
}

function aws-get-created-meshes {
    aws appmesh list-meshes
}

function aws-create-mesh {
    validate-param "mesh name"
    aws appmesh create-mesh --mesh-name $1
}

function aws-create-policy {
    validate-param "policy name(and file name)"
    aws iam create-policy --policy-name $1 --policy-document file://{$1}
}

function aws-create-virtual-node {
    validate-param "json node description file"
    aws appmesh create-virtual-node --cli-input-json file://{$1}
}
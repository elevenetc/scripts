#!/usr/bin/env bash

function ios-search-db() {
  validate-param "db name" $1
  dbName=$1
  devicesDir=$HOME/Library/Developer/CoreSimulator/Devices
  pathToDb=$(find "$devicesDir" -type f -name "$dbName")
  echo $pathToDb
}

function ios-open-db() {
  validate-param "db name" $1
  dbName=$1
  pathToDb=$(ios-search-db "$dbName")
  echo $pathToDb
  open $pathToDb
}
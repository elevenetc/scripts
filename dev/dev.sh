#!/usr/bin/env bash

function dev-java-lines {
    find . -name "*.java" -exec grep "[a-zA-Z0-9{}]" {} \; | wc -l
}

function dev-kotlin-lines {
    find . -name "*.kt" -exec grep "[a-zA-Z0-9{}]" {} \; | wc -l
}

function dev-xml-lines {
    find . -name "*.xml" | wc -l
}

function dev-android-lines {
    echo "kotlin lines: $(dev-kotlin-lines)"
    echo "java lines: $(dev-java-lines)"
    echo "xml lines: $(dev-xml-lines)"
}


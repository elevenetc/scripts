#!/usr/bin/env bash
function media-compress-images-to-700 {
    sips --resampleWidth 700 *
}

# brew install imagemagick
function media-jpgs-to-pdf {
    convert *.jpg images.pdf
}

function media-compress-and-send {

    subj=$1
    address=$2

    media-compress-images-to-700
    media-jpgs-to-pdf
    uuencode ./images.pdf | mail -s "{$subj}" "{$address}"
}
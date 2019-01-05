#!/usr/bin/env bash

function media-compress-images {
    validate-param "width" $1
    width=$1
    sips --resampleWidth ${width} *
}

function media-compress-images-to-700 {
    media-compress-images 700
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

function media-merge-pdfs {
    mergedFileName=$1
    /System/Library/Automator/Combine\ PDF\ Pages.action/Contents/Resources/join.py --output ${mergedFileName}.pdf *.pdf
}

function media-jpg-to-mp4 {
    ffmpeg -framerate 1 -pattern_type glob -i '*.jpg' -c:v libx264 -r 30 -pix_fmt yuv420p out.mp4
}
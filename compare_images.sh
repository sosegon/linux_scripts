#!/bin/bash

adb shell screencap -p /sdcard/screenshot.png 

adb pull /sdcard/screenshot.png

convert $1 \( screenshot.png -channel A -fx '0.5' \) -flatten -resize 50% out.png

magick display out.png
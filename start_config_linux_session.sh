#!/usr/bin/bash

## The objective of this script is to set the keyboard to latam spanish,
## set the slash key to be close to the index finger, and alias git command.
## All this aimed to increase speed when typing.

setxkbmap -layout 'es,es'
echo "set spanish keyboard"
xmodmap ~/.Xmodmap.try
echo "keys set"
alias gt="git"
echo "aliased git"


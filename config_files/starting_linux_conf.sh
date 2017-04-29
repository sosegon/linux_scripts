#!/usr/bin/bash

## The objective of this script is to set the keyboard to latam spanish,
## set the slash key to be close to the index finger, and alias git command.
## All this aimed to increase speed when typing.

# privilegies
sudo chown sebastian:sebastian /mnt
echo "set privilegies for mnt"
# mount partition
sudo mount -t ext4 /dev/sda2 /mnt/linux_shared
echo "mount shared partition"
# set variables
source ~/.bashrc
echo "set variables"
# set keyboard
setxkbmap -layout 'es,es'
echo "set spanish keyboard"
# alias for git
alias gt="git"
echo "aliased git"


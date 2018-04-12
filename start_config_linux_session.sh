#!/usr/bin/bash

## The objective of this script is to set the keyboard to latam spanish,
## set the slash key to be close to the index finger, alias git command, 
## and load the partitions from the disk
## All this aimed to increase speed when typing.

# privilegies
sudo chown sebastian:sebastian /mnt
echo "set privilegies for mnt"

# mount partition
sudo mount -t ext4 /dev/sda2 /mnt/linux_shared
echo "mount shared partition"

# mount lubuntu partition
sudo mount -t ext4 /dev/sda4 /mnt/mint
echo "mount mint partition"

# set variables
source /mnt/linux_shared/shared/.bashrc
echo "set variables"

# set keyboard
setxkbmap -layout 'es,es'
echo "set spanish keyboard"

# This is giving some problems, the computer freezes.
# set keys
#xmodmap ~/.Xmodmap.try
#echo "keys set"

# alias for git
alias gt="git"
echo "aliased git"

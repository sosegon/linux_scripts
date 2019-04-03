#!/bin/bash

## The objective of this script is to set the keyboard to latam spanish,
## set the slash key to be close to the index finger, alias git command,
## and load the partitions from the disk
## All this aimed to increase speed when typing.

# Change your password in 'your_pasword'

# privilegies
echo 's3kut3' | sudo -S chown sebastian:sebastian /mnt
echo "set privilegies for mnt"

# mount partition
echo 's3kut3' | sudo -S mount -t ext4 /dev/sd$12 /mnt/linux_shared
echo "mount shared partition"

# mount lubuntu partition
echo 's3kut3' | sudo -S mount -t ext4 /dev/sd$14 /mnt/mint
echo "mount mint partition"

# set variables
source /mnt/linux_shared/shared/.bashrc
echo "set variables"

# set keyboard
setxkbmap -layout 'es,es'
echo "set spanish keyboard"

# alias for git
alias gt="git"
echo "aliased git"

# alias linux commands
alias sd="sudo docker"

# alias web server
alias pyw="python -m SimpleHTTPServer"

# alias npm install/unistall
alias ni="npm install --save"
alias nid="npm install --save-dev"
alias nu="npm uninstall --save"
alias nud="npm uninstall --save-dev"

# alias ssh-agent
alias sag 'eval "$(ssh-agent -s)'


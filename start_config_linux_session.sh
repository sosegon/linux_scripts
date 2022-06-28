#!/bin/bash

## The objective of this script is to set the keyboard to latam spanish,
## set the slash key to be close to the index finger, alias git command,
## and load the partitions from the disk
## All this aimed to increase speed when typing.

# Change your password in 'your_pasword'

# privilegies
echo 'your_pasword' | sudo -S chown sebastian:sebastian /mnt
echo "set privilegies for mnt"

# mount partition
echo 'your_pasword' | sudo -S mount -t ext4 /dev/sd$1 /mnt/linux_shared
echo "mount shared partition"

# mount lubuntu partition
echo 'your_pasword' | sudo -S mount -t ext4 /dev/sd$1 /mnt/mint
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
alias sdc="sudo docker container"
alias sdcstop="sudo docker container stop `sudo docker ps -a -q`"

# alias web server
alias pyw="python -m SimpleHTTPServer"

# alias npm install/unistall
alias ni="npm install --save"
alias nid="npm install --save-dev"
alias nu="npm uninstall --save"
alias nud="npm uninstall --save-dev"

# alias expo
alias expostart="rm -rf .expo && npm start"

# build react native apk
alias rnbuildd="react-native bundle --platform android --dev false --entry-file index.js --bundle-output android/app/src/main/assets/index.android.bundle --assets-dest android/app/src/main/res/ && cd android && ./gradlew assembleDebug && cd .."
alias rnbuildr="react-native bundle --platform android --dev false --entry-file index.js --bundle-output android/app/src/main/assets/index.android.bundle --assets-dest android/app/src/main/res/ && cd android && ./gradlew assembleRelease && cd .."
alias rndebug="react-native bundle --platform android --dev false --entry-file index.js --bundle-output android/app/src/main/assets/index.android.bundle --assets-dest android/app/src/main/res/ && npx react-native run-android && react-native log-android"

# alias yarn
alias yi="yarn add"
alias yid="yarn add --dev"
alias yu="yarn remove"
alias yud="yarn remove"

# alias ssh-agent
alias sag='eval "$(ssh-agent -s)"'

# alias source activate
alias soa='source activate'

# alias source deactivate
alias sod='source deactivate'

# export dependencies of conda env
alias conexp = 'conda env export | grep -v "^prefix: " > '

# set keyboard to spanish
alias kes='setxkbmap -layout "es,es"'

# set keyboard to english
alias ken='setxkbmap -layout "us"'

# Login to npm
alias npmu13='npm login --scope=@upstart13-com --registry=https://npm.pkg.github.com'

# git user email U13, normal
alias gtu13='git config --global  user.email svelasquez@upstart13.com'
alias gtnor='git config --global  user.email anse23@hotmail.com'

# ssh connect to vm
alias wgsnssh='ssh svelasquez@dev-wgsn-svelasquez.use1.wgsndev.com'

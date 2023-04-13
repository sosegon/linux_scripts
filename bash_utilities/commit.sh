#!/usr/local/bin/sh
# Script used to merge two github repositories keeping
# the commit history. It has to be used along with merge.sh
# The usage is the following:
# 0. merge.sh and commit.sh need to be located in the directory of
# the new repository.
# 1. Run merge.sh with the name of the repository and the new folder
# to contain its files: ./merge.sh repo_name folder_name
# 2. Manually move the files fetched from repo_name to folder_name
# 3. Run commit.sh with the name of the old repository: ./commit.sh repo_name
# 4. Input username and password
git add .
git reset HEAD merge.sh commit.sh
git commit -m "conf: Moved $1 to its unique folder"
git ps master
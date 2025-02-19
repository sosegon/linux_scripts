#!/bin/bash
"exec" "$ANACONDA/envs/organize_media/bin/python3" "$0" "$@"

import os
from os.path import isfile, join
import shutil
import argparse
from common import Clock, write_logs, print_summary, summarize_logs

def copy_to_unique(source_dir, existing_dir, new_dir, dictionary, results):
    # loop through each folder in the source directory
    for elem_name in os.listdir(source_dir):
        elem_full_name = join(source_dir, elem_name)
        if isfile(elem_full_name):
            if elem_name in dictionary:
                print('already exists: ', elem_full_name, ' -> ', dictionary[elem_name])
                shutil.copy2(dictionary[elem_name], existing_dir)
                shutil.move(join(existing_dir, elem_name), join(existing_dir, elem_full_name.replace('/', '__')))
                results.append({
                    'status': 'already_exists',
                    'existing': elem_full_name,
                    'new': dictionary[elem_name],
                })
            else:
                dictionary[elem_name] = elem_full_name
                shutil.copy2(elem_full_name, new_dir)
        else:
            copy_to_unique(elem_full_name, existing_dir, new_dir, dictionary, results)
    
    return results

def main():
    parser = argparse.ArgumentParser(description='Copy files from a folders tree to a unique folder')
    parser.add_argument('folder_source', help='Original folder containing the media')
    parser.add_argument('folder_existing', help='Destination folder to store the existing media')
    parser.add_argument('folder_new', help='Destination folder to store the new media')
    parser.add_argument('--log_file', '-l', type=str, default='./copy_to_unique.csv', help='Log file')

    args = parser.parse_args()
    source_dir = args.folder_source
    existing_dir = args.folder_existing
    new_dir = args.folder_new
    
    dictionary = {}
    results = []
    copy_to_unique(source_dir, existing_dir, new_dir, dictionary, results)
    write_logs(args.log_file, results, ['status', 'existing', 'new'])
    print_summary(summarize_logs(results, ['already_exists']))

if __name__ == '__main__':
    print('copying files started')
    clock = Clock()
    clock.show()
    main()
    clock.hide()
    clock.print_time()
    print('copying files finished')


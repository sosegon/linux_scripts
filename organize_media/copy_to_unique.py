#!/bin/bash
"exec" "$ANACONDA/envs/organize_media/bin/python3" "$0" "$@"

import os
from os.path import isfile, join
import shutil
import argparse
from common import Clock, write_logs, print_summary, summarize_logs

def copy_from_folder_to_unique_folder(source_dir, target_dir, results):
    # loop through each folder in the source directory
    for elem_name in os.listdir(source_dir):
        elem_full_name = join(source_dir, elem_name)
        if isfile(elem_full_name):
            # copy the file to the target directory
            shutil.copy2(elem_full_name, target_dir)
            # add the file name to the results list
            results.append({
                'status': 'copied',
                'original_path': elem_full_name,
                'new_path': os.path.join(target_dir, elem_name),
            })
        else:
            copy_from_folder_to_unique_folder(elem_full_name, target_dir, results)
    
    return results

def main():
    parser = argparse.ArgumentParser(description='Copy files from a folders tree to a unique folder')
    parser.add_argument('folder_source', help='Original folder containing the media')
    parser.add_argument('folder_destination', help='Destination folder to store the organized media')
    parser.add_argument('--log_file', '-l', type=str, default='./copy_to_unique.csv', help='Log file')

    args = parser.parse_args()
    source_dir = args.folder_source
    target_dir = args.folder_destination

    results = []
    copy_from_folder_to_unique_folder(source_dir, target_dir, results)
    write_logs(args.log_file, results, ['status', 'original_path', 'new_path'])
    print_summary(summarize_logs(results, ['copied']))


if __name__ == '__main__':
    print('copying files started')
    clock = Clock()
    clock.show()
    main()
    clock.hide()
    clock.print_time()
    print('copying files finished')


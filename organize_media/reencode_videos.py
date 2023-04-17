#!/bin/bash
"exec" "$ANACONDA/envs/organize_media/bin/python3" "$0" "$@"
import argparse
import os
from os import listdir
from os.path import isfile, join
import subprocess
import mimetypes
import csv
from common import Clock, verify_folder, print_summary, summarize_logs

def write_logs(logs_file, logs):
    # write to file
    with open(logs_file, 'w') as f:
        header = ['status', 'original_file', 'original_size', 'new_file', 'new_size', 'error']
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        writer.writerows(logs)
    f.close()

def reencode_videos(root_folder, folder_name, videos_processed=[], overwrite=False):
    for elem_name in listdir(folder_name):
        elem_full_name = join(folder_name, elem_name)
        if isfile(elem_full_name):
            new_elem_full_name =  os.path.join(root_folder + '_reencoded', os.path.relpath(elem_full_name, root_folder)) if not overwrite else elem_full_name
            file_size = os.path.getsize(elem_full_name)
            try:
                typefile = mimetypes.guess_type(elem_full_name)[0]
                if typefile is not None and typefile.find('video') != -1:
                    verify_folder(os.path.dirname(new_elem_full_name), '')
                    metadata_creation_time = subprocess.check_output([
                        "date", "-u", "+%Y-%m-%dT%H:%M:%SZ", "-d", 
                        "@" + str(int(os.stat(elem_full_name).st_mtime))
                    ]).decode().strip()
                    command = [
                        'ffmpeg',
                        '-i',
                        elem_full_name,
                        '-vcodec',
                        'libx265',
                        '-crf',
                        '28',
                        '-map_metadata',
                        '0',
                        '-metadata',
                        f"creation_time={metadata_creation_time}",
                        new_elem_full_name
                    ]
                    subprocess.call(command)
                    r = {
                        'status': 'REENCODED',
                        'original_file': elem_full_name,
                        'original_size': file_size,
                        'new_file': new_elem_full_name,
                        'new_size': os.path.getsize(new_elem_full_name),
                        'error': ''
                    }
                    videos_processed.append(r)
            except Exception as e:
                print('Error reencoding', elem_name, e)
                r = {
                    'status': 'ERROR',
                    'original_file': elem_full_name,
                    'original_size': file_size,
                    'new_file': 'N/A',
                    'new_size': 'N/A',
                    'error': 'Error reencoding video'
                }
                videos_processed.append(r)
        else:
            reencode_videos(root_folder, elem_full_name, videos_processed, overwrite)

def main():
    parser = argparse.ArgumentParser(description='Reencode videos')
    parser.add_argument('folder', help='Folder containing the videos')
    parser.add_argument('--log_file', '-l', type=str, default='./reencode_videos.csv', help='Log file')
    parser.add_argument('--overwrite', '-o', type=bool, default=False, help='Overwrites original videos')

    args = parser.parse_args()

    folder_name = args.folder
    log_file = args.log_file
    overwrite = args.overwrite

    results = []
    reencode_videos(folder_name, folder_name, results, overwrite)
    write_logs(log_file, results)
    print_summary(summarize_logs(results, ['REENCODED', 'ERROR']))


if __name__ == '__main__':
    print('reencoding videos started')
    clock = Clock()
    clock.show()
    main()
    clock.hide()
    clock.print_time()
    print('reencoding videos completed')
#!/bin/bash
"exec" "$ANACONDA/envs/organize_media/bin/python3" "$0" "$@"
import argparse
import os
from os import listdir
from os.path import isfile, join
import subprocess
import mimetypes
import csv
from common import Clock, get_exif_date, verify_folder, print_summary, summarize_logs

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
                    # Get metadata to insert into reencoded video
                    metadata_creation_time = subprocess.check_output([
                        "date", "-u", "+%Y-%m-%dT%H:%M:%SZ", "-d", 
                        "@" + str(int(os.stat(elem_full_name).st_mtime))
                    ]).decode().strip()
                    exif_date = get_exif_date(elem_full_name)
                    if 'original_date' in exif_date and exif_date['original_date'] != '':
                        metadata_creation_time = exif_date['original_date']
                    elif 'create_date' in exif_date and exif_date['create_date'] != '':
                        metadata_creation_time = exif_date['create_date']
                    elif 'modify_date' in exif_date and exif_date['modify_date'] != '':
                        metadata_creation_time = exif_date['modify_date']
                    print(metadata_creation_time)
                    # Reencode
                    command = [
                        'ffmpeg',
                        '-i',
                        elem_full_name,
                        '-vcodec',
                        'libx265',
                        '-crf',
                        '28',
                        '-movflags',
                        'use_metadata_tags',
                        '-map_metadata',
                        '0',
                        '-metadata',
                        f"creation_time={metadata_creation_time}",
                        '-metadata',
                        f"modification_time={metadata_creation_time}",
                        '-metadata',
                        'reencodedBySosegon=true',
                        new_elem_full_name
                    ]
                    subprocess.call(command)
                    # Update dates
                    command = [
                        'exiftool',
                        f"-CreateDate={metadata_creation_time}",
                        new_elem_full_name
                    ]
                    subprocess.call(command)
                    command = [
                        'exiftool',
                        f"-AllDates={metadata_creation_time}",
                        new_elem_full_name
                    ]
                    subprocess.call(command)
                    command = [
                        'exiftool',
                        f"-FileModifyDate={metadata_creation_time}",
                        new_elem_full_name
                    ]
                    subprocess.call(command)
                    # Remove original file
                    backup_new_elem_full_name = new_elem_full_name + '_original'
                    if os.path.exists(backup_new_elem_full_name):
                        os.remove(backup_new_elem_full_name)
                    # Log
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
#!/bin/bash
"exec" "$ANACONDA/envs/organize_media/bin/python3" "$0" "$@"

import argparse
import os
from os import listdir
from os.path import isfile, join
import datetime
import mimetypes
import ffmpeg
from common import verify_folder, copy_file_to_folder, exception_handler, write_logs

def copy_videos_by_date(folder_name, destination_folder, videos_processed):
    for elem_name in listdir(folder_name):
        elem_full_name = join(folder_name, elem_name)

        if isfile(elem_full_name):
            try:
                typefile = mimetypes.guess_type(elem_full_name)[0]
                if typefile is not None and typefile.find('video') != -1:
                    probe = ffmpeg.probe(elem_full_name)
                    creation_time = next((stream['tags']['creation_time'] for stream in probe['streams'] if 'tags' in stream and 'creation_time' in stream['tags']), None)
                    has_metadata = True
                    if creation_time is not None:
                        try:
                            original_date = datetime.datetime.strptime(creation_time, '%Y-%m-%dT%H:%M:%S.%fZ').strftime('%Y-%m')
                        except ValueError:
                            try:
                                original_date = datetime.datetime.strptime(creation_time, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m')
                            except ValueError:
                                raise Exception("Unable to parse creation time")
                    else:
                        original_date = datetime.datetime.fromtimestamp(os.path.getmtime(elem_full_name)).strftime('%Y-%m')
                        has_metadata = False
                    folder_to_copy = verify_folder(destination_folder, original_date)
                    result = copy_file_to_folder(elem_full_name, elem_name, folder_to_copy, original_date, 'video', has_metadata)
                    videos_processed.append(result)
                    continue
            except Exception as e:
                print(e)
                videos_processed.append(exception_handler(elem_full_name))
                continue
        else:
            copy_videos_by_date(elem_full_name, destination_folder, videos_processed)
    
    return videos_processed

def main():
    parser = argparse.ArgumentParser(description='Organize videos chronologically in folders by year and month')
    parser.add_argument('folder_source', help='Original folder containing the videos')
    parser.add_argument('folder_destination', help='Destination folder to store the organized videos')
    parser.add_argument('--log_file', '-l', type=str, default='./organize_videos.csv', help='Log file')

    args = parser.parse_args()

    folder_source = args.folder_source
    folder_destination = args.folder_destination
    log_file = args.log_file

    results = []
    copy_videos_by_date(folder_source, folder_destination, results)
    write_logs(log_file, results)

if __name__ == '__main__':
    main()
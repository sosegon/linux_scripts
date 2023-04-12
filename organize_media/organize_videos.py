'''
    File name: organize_videos.py

    Author: Sebastian Velasquez

    Date created: 2023/04/12

    Date last modified: 2023/04/12

    Python Version: 3.6.9

    License. The MIT License | https://opensource.org/licenses/MIT

    Description: This script copies video files from one location to another and organizes them into
    folders by their creation date. It uses FFmpeg to extract the creation time metadata from video files
    and falls back to the last modification time if that metadata is not present. The copied files are
    organized into subfolders named after the year and month of their creation.

    Usage: In a Linux terminal, go to the location of the script and type the following:

    python organize_videos.py /path/to/source/folder /path/to/destination/folder /path/to/log/file

    In the Windows command prompt, type like the following:

    python organize_videos.py "C:\Path\To\Source\Folder" "C:\Path\To\Destination\Folder" "C:\Path\To\Log\File"

    The first argument is the path to the source folder containing the original video files.
    The second argument is the path to the destination folder where the copied video files will be located.
    The third argument is the path to the log file where the list of processed files will be written.
'''
import sys
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
                        original_date = datetime.datetime.strptime(creation_time, '%Y-%m-%dT%H:%M:%S.%fZ').strftime('%Y-%m')
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

results = []
copy_videos_by_date(sys.argv[1], sys.argv[2], results)
write_logs(sys.argv[3], results)
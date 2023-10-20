#!/bin/bash
"exec" "$ANACONDA/envs/organize_media/bin/python3" "$0" "$@"

import argparse
import os
from os import listdir
from os.path import isfile, join
import datetime
import mimetypes
from common import Clock, date_to_year_month, get_exif_date, verify_folder, copy_file_to_folder, exception_handler, write_logs, summarize_logs, print_summary

def copy_videos_by_date(folder_name, destination_folder, videos_processed):
    for elem_name in listdir(folder_name):
        elem_full_name = join(folder_name, elem_name)

        if isfile(elem_full_name):
            try:
                typefile = mimetypes.guess_type(elem_full_name)[0]
                if typefile is not None and typefile.find('video') != -1:
                    exif_date = get_exif_date(elem_full_name)
                    has_exif = True
                    if 'original_date' in exif_date and exif_date['original_date'] != '':
                        original_date = date_to_year_month(exif_date['original_date'])
                    elif 'create_date' in exif_date and exif_date['create_date'] != '':
                        original_date = date_to_year_month(exif_date['create_date'])
                        has_exif = False
                    elif 'modify_date' in exif_date and exif_date['modify_date'] != '':
                        original_date = date_to_year_month(exif_date['modify_date'])
                        has_exif = False
                    else:
                        # original_date = datetime.datetime.fromtimestamp(os.path.getmtime(elem_full_name)).strftime('%Y-%m')
                        has_exif = False
                        m_time = os.path.getmtime(elem_full_name)
                        dt = datetime.datetime.fromtimestamp(m_time).timetuple()
                        #convert month to 2 digits
                        month = str(dt.tm_mon)
                        if len(month) == 1:
                            month = '0' + month
                        original_date = "%s-%s" % (dt.tm_year, month)
                    folder_to_copy = verify_folder(destination_folder, original_date)
                    result = copy_file_to_folder(elem_full_name, elem_name, folder_to_copy, original_date, 'video', has_exif)
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
    print_summary(summarize_logs(results, ['SKIPPED', 'COPIED']))

if __name__ == '__main__':
    print('organizing videos started')
    clock = Clock()
    clock.show()
    main()
    clock.hide()
    clock.print_time()
    print('organizing videos completed')
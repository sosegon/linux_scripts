#!/bin/bash
"exec" "$ANACONDA/envs/organize_media/bin/python3" "$0" "$@"

import argparse
import os
from os import listdir
from os.path import isfile, join
from PIL import Image, ExifTags
import datetime
import mimetypes
import ffmpeg
from common import verify_media_folder, copy_file_to_folder, exception_handler, write_logs

def get_exif_data(image):
    exif_data = {}
    info = image._getexif()
    if info:
        for tag, value in info.items():
            decoded = ExifTags.TAGS.get(tag, tag)
            if decoded == "GPSInfo":
                gps_data = {}
                for t in value:
                    sub_decoded = ExifTags.GPSTAGS.get(t, t)
                    gps_data[sub_decoded] = value[t]

                exif_data[decoded] = gps_data
            else:
                exif_data[decoded] = value

    return exif_data

def date_to_year_month(date):
    return date[:4] + '-' + date[5:7]

def copy_media_by_date(folder_name, destination_folder, media_processed):
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
                    folder_to_copy = verify_media_folder('videos', destination_folder, original_date)
                    result = copy_file_to_folder(elem_full_name, elem_name, folder_to_copy, original_date, 'video', has_metadata)
                    media_processed.append(result)
                    continue
                elif typefile is None or typefile.find('image') != -1:
                    image = Image.open(elem_full_name)
                    exif_data = get_exif_data(image)
                    has_exif = True
                    if 'DateTimeOriginal' in exif_data and exif_data['DateTimeOriginal'] != '':
                        original_date = date_to_year_month(exif_data['DateTimeOriginal'])
                    else:
                        has_exif = False
                        m_time = os.path.getmtime(elem_full_name)
                        dt = datetime.datetime.fromtimestamp(m_time).timetuple()
                        #convert month to 2 digits
                        month = str(dt.tm_mon)
                        if len(month) == 1:
                            month = '0' + month
                        original_date = "%s-%s" % (dt.tm_year, month)

                    # verify the folder
                    folder_to_copy = verify_media_folder('fotos', destination_folder, original_date)
                    # copy the image
                    result = copy_file_to_folder(elem_full_name, elem_name, folder_to_copy, original_date, 'image', has_exif)
                    media_processed.append(result)
                    continue
                elif typefile is not None and typefile.find('audio') != -1:
                    probe = ffmpeg.probe(elem_full_name)
                    creation_time = next((stream['tags']['creation_time'] for stream in probe['streams'] if 'tags' in stream and 'creation_time' in stream['tags']), None)
                    has_metadata = True
                    if creation_time is not None:
                        original_date = datetime.datetime.strptime(creation_time, '%Y-%m-%dT%H:%M:%S.%fZ').strftime('%Y-%m')
                    else:
                        original_date = datetime.datetime.fromtimestamp(os.path.getmtime(elem_full_name)).strftime('%Y-%m')
                        has_metadata = False
                    folder_to_copy = verify_media_folder('audios', destination_folder, original_date)
                    result = copy_file_to_folder(elem_full_name, elem_name, folder_to_copy, original_date, 'audio', has_metadata)
                    media_processed.append(result)
                    continue
            
            except Exception as e:
                print(e)
                media_processed.append(exception_handler(elem_full_name))
                continue
        else:
            copy_media_by_date(elem_full_name, destination_folder, media_processed)

    return media_processed

def main():
    parser = argparse.ArgumentParser(description='Organize media chronologically in folders by year and month')
    parser.add_argument('folder_source', help='Original folder containing the media')
    parser.add_argument('folder_destination', help='Destination folder to store the organized media')
    parser.add_argument('--log_file', '-l', type=str, default='./organize_media.csv', help='Log file')

    args = parser.parse_args()

    folder_source = args.folder_source
    folder_destination = args.folder_destination
    log_file = args.log_file

    results = []
    copy_media_by_date(folder_source, folder_destination, results)
    write_logs(log_file, results)

if __name__ == '__main__':
    main()
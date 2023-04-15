#!/bin/bash
"exec" "$ANACONDA/envs/organize_media/bin/python3" "$0" "$@"

import argparse
import os
from os import listdir
from os.path import isfile, join
from PIL import Image, ExifTags
import datetime
import mimetypes
from common import verify_folder, copy_file_to_folder, exception_handler, write_logs

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
        
def copy_pictures_by_date(folder_name, destination_folder, images_processed):
    for elem_name in listdir(folder_name):
        elem_full_name = join(folder_name, elem_name)

        if isfile(elem_full_name):
            try:
                typefile = mimetypes.guess_type(elem_full_name)[0]
                if typefile is None or typefile.find('image') != -1:
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
                    folder_to_copy = verify_folder(destination_folder, original_date)
                    # copy the image
                    result = copy_file_to_folder(elem_full_name, elem_name, folder_to_copy, original_date, 'image', has_exif)
                    images_processed.append(result)
                    continue
            except Exception as e:
                print(e)
                images_processed.append(exception_handler(elem_full_name))
                continue
        else:
            copy_pictures_by_date(elem_full_name, destination_folder, images_processed)

    return images_processed

def main():
    parser = argparse.ArgumentParser(description='Organize pictures chronologically in folders by year and month')
    parser.add_argument('folder_source', help='Original folder containing the pictures')
    parser.add_argument('folder_destination', help='Destination folder to store the organized pictures')
    parser.add_argument('--log_file', '-l', type=str, default='./organize_pictures.csv', help='Log file')

    args = parser.parse_args()

    folder_source = args.folder_source
    folder_destination = args.folder_destination
    log_file = args.log_file

    results = []
    copy_pictures_by_date(folder_source, folder_destination, results)
    write_logs(log_file, results)

if __name__ == '__main__':
    main()
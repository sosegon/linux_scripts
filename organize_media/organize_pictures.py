'''
    File name: organize_pictures.py

    Author: Sebastian Velasquez

    Date created: 2023/04/12

    Date last modified: 2023/04/12

    Python Version: 3.6.9

    License. The MIT License | https://opensource.org/licenses/MIT

    Description: The purpose of this script is to copy pictures from one
    location to another and organize them by date. The script extracts the
    date the picture was taken from the EXIF data, or if that is not available,
    the date the file was last modified. The pictures are then copied to a
    folder named after the date they were taken.

    Usage: In a Linux terminal, go to the location of the script and type the following:

    python  organize_pictures.py /path/to/source/folder /path/to/destination/folder /path/to/log/file.log

    In the command line of Windows, type like the following:

    python  organize_pictures.py "C:\path\to\source\folder" "C:\path\to\destination\folder" "C:\path\to\log\file.log"

    The first argument is the source folder that contains the original pictures.
    The second argument is the destination folder where the new pictures will be located.
    The third argument is the path to the log file where information about the copy process will be stored.
'''
import sys
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
                    if 'DateTimeOriginal' in exif_data and exif_data['DateTimeOriginal'] is not '':
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
    
results = []
copy_pictures_by_date(sys.argv[1], sys.argv[2], results)
write_logs(sys.argv[3], results)
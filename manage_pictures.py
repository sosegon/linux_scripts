from re import I
import sys
import os
from os import listdir
from os.path import isfile, join
from PIL import Image, ExifTags
import shutil
import csv
import datetime
import mimetypes

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

def get_full_date(file_path):
    return datetime.datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%Y-%m-%d_%H-%M-%S')

def verify_folder(destination_folder, original_date):
    folder_to_copy = join(destination_folder, original_date)
    if not os.path.exists(folder_to_copy):
        os.makedirs(folder_to_copy)
    return folder_to_copy

def exception_handler(original_file_path):
    return {
        'status': 'SKIPPED',
        'type': 'other',
        'date': '',
        'original': original_file_path,
        'new': '',
        'exif': False,
        'error': 'error processing file'
    }

def copy_file_to_folder(original_file_path, new_file_name, folder_to_copy, original_date, type, exif=True):
    new_file_path = join(folder_to_copy, new_file_name)
    if new_file_name not in listdir(folder_to_copy):
        shutil.copy2(original_file_path, new_file_path)
        return {
            'status': 'COPIED',
            'type': type,
            'date': original_date,
            'original': original_file_path,
            'new': new_file_path,
            'exif': exif,
            'error': ''
        }
    else:
        full_date_1 = get_full_date(original_file_path)
        full_date_2 = get_full_date(new_file_path)

        if full_date_1 != full_date_2:
            # split file name in name and extension
            name, extension = os.path.splitext(new_file_name)
            # add the date to the file name
            new_file_name2 = name + '_' + full_date_1 + extension
            new_file_path2 = join(folder_to_copy, new_file_name2)
            shutil.copy2(original_file_path, new_file_path2)

        return {
            'status': 'COPIED' if full_date_1 != full_date_2 else 'SKIPPED',
            'type': type,
            'date': original_date,
            'original': original_file_path,
            'new': new_file_path2 if full_date_1 != full_date_2 else new_file_path,
            'exif': exif,
            'error': 'file already exists in the folder with a different date' if full_date_1 != full_date_2 else 'file already exists in the folder'
        }
        
def copy_pictures_by_date(folder_name, destination_folder, images_processed):
    for elem_name in listdir(folder_name):
        elem_full_name = join(folder_name, elem_name)

        if isfile(elem_full_name):
            # if it is a video
            try:
                typefile = mimetypes.guess_type(elem_full_name)[0]
                if  typefile is not None and typefile.find('video') != -1:
                    # get the date of the video
                    original_date = datetime.datetime.fromtimestamp(os.path.getmtime(elem_full_name)).strftime('%Y-%m')
                    # verify the folder
                    folder_to_copy = verify_folder(destination_folder, original_date)
                    if not os.path.exists(folder_to_copy):
                        os.makedirs(folder_to_copy)
                    # copy the video
                    result = copy_file_to_folder(elem_full_name, elem_name, folder_to_copy, original_date, 'video', False)
                    images_processed.append(result)
                    continue
            except:
                print(e)
                images_processed.append(exception_handler(elem_full_name))
                continue 
            #if it is a picture
            try:
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

def write_logs(logs_file, logs):
    # write to file
    with open(logs_file, 'w') as f:
        header = ['status', 'type', 'date', 'original', 'new', 'error', 'exif']
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        writer.writerows(logs)
    f.close()
    
results = []
copy_pictures_by_date(sys.argv[1], sys.argv[2], results)
write_logs(sys.argv[3], results)
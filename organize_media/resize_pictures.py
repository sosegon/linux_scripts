import sys
import os
from os import listdir
from os.path import isfile, join
import subprocess
import mimetypes
import csv

def write_logs(logs_file, logs):
    # write to file
    with open(logs_file, 'w') as f:
        header = ['status', 'file', 'original_size', 'new_size', 'error']
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        writer.writerows(logs)
    f.close()

def resize_pictures(folder_name,  max_size=1e6, images_processed=[]):
    for elem_name in listdir(folder_name):
        elem_full_name = join(folder_name, elem_name)
        file_size = os.path.getsize(elem_full_name)
        if isfile(elem_full_name) and file_size > max_size:
            try:
                typefile = mimetypes.guess_type(elem_full_name)[0]
                if typefile is not None and typefile.find('image') != -1:
                    command = ['convert', elem_full_name, '-define', 'jpeg:extent=1MB', elem_full_name]
                    subprocess.call(command)
                    new_file_size = os.path.getsize(elem_full_name)
                    r = {
                        'status': 'RESIZED',
                        'file': elem_full_name,
                        'original_size': f'{file_size / (1024 * 1024):.2f} MB',
                        'new_size': f'{new_file_size / (1024 * 1024):.2f} MB',
                        'error': ''
                    }
                    images_processed.append(r)
            except Exception as e:
                print('Error resizing', elem_name, e)
                r = {
                    'status': 'RESIZED',
                    'file': elem_full_name,
                    'original_size':f'{file_size / (1024 * 1024)} MB',
                    'new_size': '~MB',
                    'error': 'Error processing file'
                }
                images_processed.append(r)
        elif not isfile(elem_full_name):
            resize_pictures(elem_full_name, max_size, images_processed)
        
results = []
resize_pictures(sys.argv[1], int(sys.argv[2]), results)
write_logs(sys.argv[3], results)
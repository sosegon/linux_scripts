import sys
import os
from os import listdir
from os.path import isfile, join
import subprocess
import mimetypes
import csv
import re

def write_logs(logs_file, logs):
    # write to file
    with open(logs_file, 'w') as f:
        header = ['status', 'file', 'original_size', 'new_size', 'error']
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        writer.writerows(logs)
    f.close()

suffixes = {
    'B': 1,
    'KB': 10**3,
    'MB': 10**6,
    'GB': 10**9,
    'TB': 10**12
}

def convert_to_bytes(size_str):
    size_str = size_str.upper()
    match = re.search(r'^(\d+)([A-Z]+)$', size_str)
    if not match:
        raise ValueError('Invalid size string')
    size_num = int(match.group(1))
    size_suffix = match.group(2)
    if size_suffix not in suffixes:
        raise ValueError('Invalid suffix')
    bytes = size_num * suffixes[size_suffix]
    return bytes

def resize_pictures(folder_name,  max_size_str='1MB', images_processed=[]):
    max_size = convert_to_bytes(max_size_str)
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
            resize_pictures(elem_full_name, max_size_str, images_processed)
        
results = []
resize_pictures(sys.argv[1], sys.argv[2], results)
write_logs(sys.argv[3], results)
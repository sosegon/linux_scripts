import os
from os import listdir
from os.path import join
import datetime
import shutil
import csv
import time
import threading

class Clock:
    def __init__(self):
        self.hidden = True
        self.counter = 0
        self.start_time = 0
        self.end_time = 0

    def show(self):
        self.hidden = False
        self.start_time = datetime.datetime.now()
        t = threading.Thread(target=self._gui_thread)
        t.start()

    def _gui_thread(self):
        while not self.hidden:
            self.counter += 1
            if self.counter % 4 == 1:
                print("\ ", end='\r')
            elif self.counter % 4 == 2:
                print("|", end='\r')
            elif self.counter % 4 == 3:
                print("/", end='\r')
            else:
                print("-", end='\r')
            time.sleep(0.1)

    def hide(self):
        self.hidden = True
        self.end_time = datetime.datetime.now()

    def print_time(self):
        # calculate the difference between the start and end times
        delta = self.end_time - self.start_time

        # extract the individual components of the timedelta object
        hours, remainder = divmod(delta.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        microseconds = delta.microseconds

        # format the components as a string using f-strings
        time_str = f"total time: {hours} hours {minutes} mins {seconds}.{microseconds // 1000} secs"

        print(time_str)

def summarize_logs(logs, keys = []):
    log_summary = {}
    for key in keys:
        filtered_logs = filter(lambda x: x['status'] == key, logs)
        log_summary[key.lower()] = len(list(filtered_logs))
    return log_summary

def print_summary(summary):
    # iterate over the keys and values of the dictionary
    print('================SUMMARY================')
    for key, value in summary.items():
        # use an f-string to print the key and value in the desired format
        print(f"{key} files: {value}")
    print('=======================================')

def write_logs(logs_file, logs, header=['status', 'type', 'date', 'original', 'new', 'error', 'exif']):
    # write to file
    with open(logs_file, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        writer.writerows(logs)
    f.close()

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

def verify_folder(destination_folder, original_date):
    folder_to_copy = join(destination_folder, original_date)
    if not os.path.exists(folder_to_copy):
        os.makedirs(folder_to_copy)
    return folder_to_copy

def verify_media_folder(file_type, destination_folder, original_date):
    folder_to_copy = join(destination_folder, file_type, original_date)
    if not os.path.exists(folder_to_copy):
        os.makedirs(folder_to_copy)
    return folder_to_copy


def get_full_date(file_path):
    return datetime.datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%Y-%m-%d_%H-%M-%S')

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
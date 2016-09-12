'''
    File name: file_folder_utils.py

    Author: Sebastian Velasquez

    Date created: 2016/09/11

    Date last modified: 2016/09/11

    Python Version: 2.7

    License. The MIT License | https://opensource.org/licenses/MIT

    Description: script with functions to play with files and folders
'''
import platform
from os import listdir
from os.path import isfile, join

def normalize_folder_name(name):
    if 'Linux' in platform.system():
        if name.endswith('/'):
            return name
        else:
            return name + '/' 

    elif 'Windows' in platform.system():
        if name.endswith('\\'):
            return name
        else: 
            return name + '\\'

def get_file_names_in_folder(folder_name):
    file_names = []

    for elem_name in listdir(folder_name):

        elem_full_name = join(folder_name, elem_name)

        if isfile(elem_full_name):
            file_names.append(elem_full_name)
        else:
            file_names = file_names + get_file_names_in_folder(elem_full_name)

    return file_names

def get_file_simple_name(file_name):
    if 'Linux' in platform.system():
        if file_name.endswith('/'):
            return file_name.split('/')[-2]
        else:
            return file_name.split('/')[-1]

    elif 'Windows' in platform.system():
        if file_name.endswith('\\'):
            return file_name.split('\\')[-2]
        else: 
            return file_name.split('\\')[-1]

from os import listdir
from os.path import isfile, join
import shutil
import sys
import platform

def read_files_in_folder(source_folder, destination_folder, file_extension, character_to_split):
    destination_folder = process_destination_folder(destination_folder)
    for f in listdir(source_folder):
        if isfile(join(source_folder, f)) and f.endswith("." + file_extension):
            new_name = create_file_name(f, character_to_split)
            if new_name is False:
                print "File " + f + " could not be copied. Character " + character_to_split + " not found in name."
            else:
                full_new_name = destination_folder + new_name
                shutil.copyfile(f, full_new_name)
                print "File " + f + " succesfully copied as " + full_new_name


def create_file_name(name, split_character):
    index = name.rfind(split_character)
    if index >= 0:
        return name[index+1:]
    else:
        return False

def process_destination_folder(name):
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

read_files_in_folder(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])


'''
    File name: copy_files_new-name.py

    Author: Sebastian Velasquez

    Date created: 2016/02/16

    Date last modified: 2016/02/16

    Python Version: 2.7

    License. The MIT License | https://opensource.org/licenses/MIT

    Description: The purpose of this script is to copy the files from
    one location to another with the option to reduce the name of the 
    files given a character.

    Usage: In a linux terminal, go to the location of the script
    and type the following: 

    python copy_files_new_name.py /home/user_name/Pictures /home/user_name/Documents jpg _

    In the command line of windows, type like the following:

    python copy_files_new_name.py "C:\Users\user_name\My Images" "C:\Users\user_name" jpg _
    
    The first argument is the source folder that contains the original files.
    The second argument is the destination forlder where the new files will be located.
    The third argument is the file extension. All the files of that type will be copied.
    The last argument is the character to generate the name of the new files. For example,
    a file named /home/user_name/Pictures/my_image.jgp will generate 
    a file called /home/user_name/Documents/image.jpg
'''
from os import listdir
from os.path import isfile, join
import shutil
import sys
import platform

def read_files_in_folder(source_folder, destination_folder, file_extension, character_to_split):
    destination_folder = process_destination_folder(destination_folder)
    for f in listdir(source_folder):
        prev_full_name = join(source_folder, f)
        if isfile(prev_full_name) and f.endswith("." + file_extension):
            new_name = create_file_name(f, character_to_split)
            if new_name is False:
                print "File " + prev_full_name + " could not be copied. Character " + character_to_split + " not found in name."
            else:
                full_new_name = destination_folder + new_name
                #print full_new_name
                shutil.copyfile(prev_full_name, full_new_name)
                print "File " + prev_full_name + " succesfully copied as " + full_new_name


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

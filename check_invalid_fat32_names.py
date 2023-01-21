import os
import sys

def is_valid_fat32(filename):
    invalid_chars = '\/:*?"<>|'
    return all(c not in invalid_chars for c in filename)

def list_invalid_fat32(directory):
    invalid_filenames = []
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            if not is_valid_fat32(filename):
                invalid_filenames.append(os.path.join(dirpath, filename))
    return invalid_filenames

directory = sys.argv[1]
invalid_filenames = list_invalid_fat32(directory)

if invalid_filenames:
    print("The following filenames contain invalid characters for the FAT32 file system:")
    for filename in invalid_filenames:
        print(filename)
else:
    print("No invalid filenames were found.")

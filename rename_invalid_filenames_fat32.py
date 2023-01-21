import os
import sys

def is_valid_fat32(filename):
    invalid_chars = '\/:*?"<>|'
    return all(c not in invalid_chars for c in filename)

def rename_invalid_fat32(directory):
    invalid_filenames = []
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            if not is_valid_fat32(filename):
                new_filename = filename
                for invalid_char in '\/:*?"<>|':
                    new_filename = new_filename.replace(invalid_char, '-')
                old_path = os.path.join(dirpath, filename)
                new_path = os.path.join(dirpath, new_filename)
                os.rename(old_path, new_path)
                invalid_filenames.append(old_path)
    return invalid_filenames

directory = sys.argv[1]
invalid_filenames = rename_invalid_fat32(directory)

if invalid_filenames:
    print("The following filenames have been renamed:")
    for filename in invalid_filenames:
        print(filename)
else:
    print("No invalid filenames were found.")

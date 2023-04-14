import sys
import os
from os import listdir
from os.path import isfile, join
from PIL import Image
import mimetypes
import piexif

def resize_pictures(folder_name,  max_size=1e6, images_processed=[]):
    for elem_name in listdir(folder_name):
        elem_full_name = join(folder_name, elem_name)
        file_size = os.path.getsize(elem_full_name)
        if isfile(elem_full_name) and file_size > max_size:
            try:
                typefile = mimetypes.guess_type(elem_full_name)[0]
                if typefile is not None and typefile.find('image') != -1:
                    image = Image.open(elem_full_name)
                    ratio = max_size / file_size
                    image = image.resize((int(image.size[0] * ratio), int(image.size[1] * ratio)), Image.ANTIALIAS)
                    exif_dict = piexif.load(image.info["exif"])
                    image.save(elem_full_name, exif=piexif.dump(exif_dict))
                    r = {
                        'status': 'RESIZED',
                        'file': elem_full_name,
                        'original_size': file_size / (1024 * 1024) + 'MB',
                        'new_size': file_size * ratio / (1024 * 1024) + 'MB',
                        'error': ''
                    }
                    images_processed.append(r)
            except Exception as e:
                print('Error resizing', elem_name, e)
                r = {
                    'status': 'RESIZED',
                    'file': elem_full_name,
                    'original_size': file_size / (1024 * 1024) + 'MB',
                    'new_size': '~MB',
                    'error': 'Error processing file'
                }
                images_processed.append(r)
        else:
            resize_pictures(elem_full_name, max_size, images_processed)
        
results = []
resize_pictures(sys.argv[1], sys.argv[2], results)
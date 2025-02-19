## Purpose

This module contains a set of scripts meant to organize media chronologically. 

## Requirements
- Preferably an Ubuntu-based distribution
- ![Anaconda 3](https://www.anaconda.com)

## Create the environment

![organize_media.yml](organize_media.yml) contains the necessary dependencies to generate a conda environment to run the python scripts to process media. Run the following command to create the environment:

```
conda env create -f organize_media.yml
```

## Activate the environment
Make sure to set an environment variable `$ANACONDA` in your system that points to the location of anaconda installation. Usually this is set in the `.bashrc` file in any Ubuntu-based system:

```
export ANACONDA=absolute_path_to_anaconda3
```

Then, run the following command:

```
source active organize_media
```

## Organize media chronologically

![organize_media.py](organize_media.py) organizes media chronologically, it receives a source directory containing the media (images, videos and audios) to be organized, and a destination directory that will contain the media organized chronologically. The destination directory will contain directories for each type of media: `audios`, `videos` and `fotos`. The files are not modified, they are simply copied to directories with the following format name `YYYY-MM` to indicate the corresponding year and month of the contained media.

**Usage**

```
./organize_media $SOURCE_DIRECTORY $DESTINATION_DIRECTORY [-L $LOG_FILE]
```

- **$SOURCE_DIRECTORY** is the absolute path to the directory containig the media to be organized
- **DESTINATION_DIRECTORY** is the absolute path to the directory that will contain the organized media
- **$LOG_FILE** is the path to the file that will contain the data about the processing of every media file. The default value is *LOCATION_OF_SCRIPT_EXECUTION/organize_media.csv*

## Update dates metadata in images
Most of the time, the metadata contains the correct date of an image. This is important because picture managers like Google Photos uses that information to present the data in the right chronological order. However, sometimes that metadata is not accurate. That happens for a variety of reasons. For example, when an image is shared through an IM application like Telegram or Whatsapp, that image is processed to optimize its size, which causes some metadata loss.

Fortunately, in many cases that metadata can be recovered (or set to be more precise) with several tools. The most practical one is ![exiftool](https://exiftool.org/). In a Linux system, the following commands can be used to set the dates metadata:

```
exiftool "-CreateDate=YYYY:MM:DD hh:mm:ss.nnn" "path_to_file/file.jpg"
exiftool "-AllDates=YYYY:MM:DD hh:mm:ss.nnn" "path_to_file/file.jpg"
exiftool "-FileModifyDate=YYYY:MM:DD hh:mm:ss.nnn" "path_to_file/file.jpg"
exiftool "-MediaCreateDate=YYYY:MM:DD hh:mm:ss.nnn" "path_to_file/file.jpg"
exiftool "-MediaModifyDate=YYYY:MM:DD hh:mm:ss.nnn" "path_to_file/file.jpg"
exiftool "-TrackCreateDate=YYYY:MM:DD hh:mm:ss.nnn" "path_to_file/file.jpg"
exiftool "-TrackModifyDate=YYYY:MM:DD hh:mm:ss.nnn" "path_to_file/file.jpg"
```

The most challenging part is to get the date the picture was taken. Fortunately, some file names contain this information. For example, the file name `IMG_20240312_221035_123.jpg` clearly indicates that date is `2024:03:12 22:10:35.123`, which can be replaced in the position `YYYY:MM:DD hh:mm:ss.nnn` in the commands above.

## Resize images
Resizing reduces the size of image files. Preferably, it must be done after the dates in the metadata of the images have been set correctly (if necessary).

![resize_pictures.py](resize_pictures.py) processes images to a given weight in bytes. By default, images are processed to weigh 1MB at most.
It adds the metadata `sizeCheckedBySosegon=true` to the resized image files.

**Usage**

```
./resize_pictures $DIRECTORY_WITH_IMAGES [-s $FILE_SIZE] [-l $LOG_FILE] [-o]
```
- **$DIRECTORY_WITH_IMAGES** is the absolute path to the directory containing the images to resize. 
- **$FILE_SIZE** is the max weigh of the output images.
- **$LOG_FILE** is the path to the file that will contain the data about the processing of every resized image. The default value is *LOCATION_OF_SCRIPT_EXECUTION/resize_pictures.csv*
- By default, the script generates a directory named *$DIRECTORY_WITH_IMAGES_resized* to store the resized images and keep the original ones. However, the original images will be completely replaced by the resized images if the flag *-o* is set to True.

## Reencode videos

Reencoding reduces the size of video files. Preferably, it must be done after the dates in the metadata of the videos have been set correctly (if necessary). 

![reencode_videos.py](reencode_videos.py) encodes videos using H.265 coder at a Constant Rate Factor of 28. It adds the metadata `reencodedBySosegon=true` to the reencoded video files.

**Usage**

```
./reencode_videos.py $DIRECTORY_WITH_VIDEOS [-l $LOG_FILE] [-o]
```

- **$DIRECTORY_WITH_VIDEOS** is the absolute path to the directory containing the videos to reencode. 

- **$LOG_FILE** is the path to the file that will contain the data about the processing of every reencoded video. The default value is *LOCATION_OF_SCRIPT_EXECUTION/reencode_videos.csv*

- By default, the script generates a directory named *$DIRECTORY_WITH_VIDEOS_reencoded* to store the reencoded videos and keep the original ones. However, the original videos will be completely replaced by the reencoded videos if the flag *-o* is set to True.

## Convert videos to mp4
Converting must be done after the dates of the videos have been correctly set (if necessary). 

![convert_to_mp4.py](convert_to_mp4.py) converts videos to mp4 format. It does not reencode anything. It adds the metadata `convertedBySosegon=true` to the converted video files.

**Usage**

```
./convert_to_mp4.py $DIRECTORY_WITH_VIDEOS [-l $LOG_FILE] [-o]
```

- **$DIRECTORY_WITH_VIDEOS** is the absolute path to the directory containing the videos to convert. 

- **$LOG_FILE** is path to the file that will contain the data about the processing of every converted video. The default value is *LOCATION_OF_SCRIPT_EXECUTION/to_mp4_videos.csv*

- By default, the script generates a directory named *$DIRECTORY_WITH_VIDEOS_converted* to store the converted videos and keep the original ones. However, the original videos will be completely replaced by the converted videos if the flag *-o* is set to True.

## Copy files to unique folder

![copy_to_unique.py](copy_to_unique.py) copies the files from a directory to another one without nested directories. 

For instance in the following tree directory:

```
folder1
 |
 |___ file1.txt
 |___ folder2
       |
       |__ file1.txt
       |__ file2.txt
       |__ file3.txt
       |__ folder3
       |    |
       |    |__ file1.txt
       |    |__ file4.txt
       |    |__ file5.txt
       |__ folder4
            |
            |__ file1.txt
            |__ file6.txt
```

It is evident that `file1.txt` is duplicated (even though the files may be different, the name is the same).

After applying the script over that directory, the output will be the following:

```
new_folder
 |
 |__ file1.txt
 |__ file2.txt
 |__ file3.txt
 |__ file4.txt
 |__ file5.txt
 |__ file6.txt
```

```
existing_folder
 |
 |__ __folder1__folder2__file1.txt
 |__ __folder1__folder2__folder3__file1.txt
 |__ __folder1__folder2__folder4__file1.txt
```

`new_folder` is a directory containing all the files under `folder1` without nested directories and without duplicates

`existing_folder` is a directory containing the duplicate files of any file under `new_folder` with their names having the full original path with `__` (double underscore) replacing `/` (slash)

**Usage**

```
./copy_to_unique $SOURCE_DIRECTORY $EXISTING_DIRECTORY $NEW_DIRECTORY [-l $LOG_FILE]
```

- **$SOURCE_DIRECTORY** is the absolute path to the directory the files to copy. 

- **$EXISTING_DIRECTORY** is the absolute path to the directory that will contain all the duplicate files of any file under *$NEW_DIRECTORY*. 

- **$NEW_DIRECTORY** is the absolute path to the directory that will contain the files from *$SOURCE_DIRECTORY* without nested directories. 

- **$LOG_FILE** is the path to the file that will contain the data about the processing of every file. The default value is *LOCATION_OF_SCRIPT_EXECUTION/copy_to_unique.csv*
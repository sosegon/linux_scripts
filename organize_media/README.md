## Reencode videos

Reencoding must be done after the dates of the videos have been correctly set (if necessary). 

![reencode_videos.py](reencode_videos.py) encodes videos using H.265 coder at a Constant Rate Factor of 28. It adds the metadata `reencodedBySosegon=true` to the reencoded video files.

**Usage**

```
./reencode_videos.py $DIRECTORY_WITH_VIDEOS [-l $LOG_FILE] [-o]
```

- **$DIRECTORY_WITH_VIDEOS** is the full path to the directory containing the videos to reencode. 

- **$LOG_FILE** is the file that will contain the data about the processing of every reencoded video. Default value is *LOCATION_OF_SCRIPT_EXECUTION/reencode_videos.csv*

- By default, the script generates a directory named *$DIRECTORY_WITH_VIDEOS_reencoded* to store the reencoded videos and keep the original ones. However, the original videos will be completely replaced by the reencoded videos if the flag *-o* is set to True.

## Convert videos to mp4
Converting must be done after the dates of the videos have been correctly set (if necessary). 

![convert_to_mp4.py](convert_to_mp4.py) converts videos to mp4 format. It does not reencode anything. It adds the metadata `convertedBySosegon=true` to the converted video files.

**Usage**

```
./convert_to_mp4.py $DIRECTORY_WITH_VIDEOS [-l $LOG_FILE] [-o]
```

- **$DIRECTORY_WITH_VIDEOS** is the full path to the directory containing the videos to convert. 

- **$LOG_FILE** is the file that will contain the data about the processing of every converted video. The default value is *LOCATION_OF_SCRIPT_EXECUTION/to_mp4_videos.csv*

- By default, the script generates a directory named *$DIRECTORY_WITH_VIDEOS_converted* to store the converted videos and keep the original ones. However, the original videos will be completely replaced by the converted videos if the flag *-o* is set to True.

## Copy files to unique folder

![copy_to_unique.py](copy_to_unique.py) copies the files from a directory to another one without nested directories. 

For instance in the following tree directory
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

- **$SOURCE_DIRECTORY** is the full path to the directory the files to copy. 

- **$EXISTING_DIRECTORY** is the full path to the directory that will contain all the duplicate files of any file under *$NEW_DIRECTORY*. 

- **$NEW_DIRECTORY** is the full path to the directory that will contain the files from *$SOURCE_DIRECTORY* without nested directories. 

- **$LOG_FILE** is the file that will contain the data about the processing of every file. The default value is *LOCATION_OF_SCRIPT_EXECUTION/copy_to_unique.csv*
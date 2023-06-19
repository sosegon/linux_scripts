#!/bin/bash

# Command to fix error when setting CreateDate
#exiftool -all= -tagsfromfile @ -all:all -unsafe -icc_profile /mnt/d/Imagenes_tamano_original_P/updating/2012-03-18\ 07.45.55.jpg

# Command to set CreateDate
#exiftool "-CreateDate=2008:11:07 11:00:00" /mnt/d/Imagenes_tamano_original_P/updating/baby3.jpg

# Command to set FileModifyDate
#exiftool -FileModifyDate="2013:07:09 22:00:00" /mnt/d/Imagenes_tamano_original_P/2005-01/DSC03908.JPG

#exiftool "-AllDates<FileModifyDate" /mnt/d/Imagenes_tamano_original_P/2008-01/*.JPG
#exiftool "-AllDates<Date" /mnt/d/Imagenes_tamano_original_P/updating/*.jpg
#exiftool "-AllDates<OriginalDate" /mnt/d/Imagenes_tamano_original_P/2008-04/*.jpg

# Command to set FileModifyDate to CreateDate
#exiftool "-FileModifyDate<CreateDate" /mnt/d/Imagenes_tamano_original_P/updating_organized/fotos/**/*.jpeg
#exiftool "-FileModifyDate<CreateDate" /mnt/d/Imagenes_tamano_original_P/updating/*.jpg
#exiftool "-FileModifyDate<CreateDate" /mnt/d/Imagenes_tamano_original_P/updating/*.jpeg
#exiftool "-FileModifyDate<CreateDate" /mnt/d/Imagenes_tamano_original_P/updating/*.JPG
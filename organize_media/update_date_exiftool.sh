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

# When using the following command
#exiftool "-CreateDate=2008:11:07 11:00:00" /mnt/d/Imagenes_tamano_original_P/updating/baby3.jpg
# Use the next ones too
#exiftool "-AllDates<CreateDate" /mnt/d/Imagenes_tamano_original_P/updating/baby3.jpg
#exiftool "-FileModifyDate<CreateDate" /mnt/d/Imagenes_tamano_original_P/updating/baby3.jpg

exiftool "-CreateDate=2024:03:16 22:20:01.102" "/mnt/d/por_organizar_de_cel_done/fotos/2024-03/IMG_20240316_222001_102.jpg"
exiftool "-AllDates=2024:03:16 22:20:01.102" "/mnt/d/por_organizar_de_cel_done/fotos/2024-03/IMG_20240316_222001_102.jpg"
exiftool "-FileModifyDate=2024:03:16 22:20:01.102" "/mnt/d/por_organizar_de_cel_done/fotos/2024-03/IMG_20240316_222001_102.jpg"
exiftool "-MediaCreateDate=2024:03:16 22:20:01.102" "/mnt/d/por_organizar_de_cel_done/fotos/2024-03/IMG_20240316_222001_102.jpg"
exiftool "-MediaModifyDate=2024:03:16 22:20:01.102" "/mnt/d/por_organizar_de_cel_done/fotos/2024-03/IMG_20240316_222001_102.jpg"
exiftool "-TrackCreateDate=2024:03:16 22:20:01.102" "/mnt/d/por_organizar_de_cel_done/fotos/2024-03/IMG_20240316_222001_102.jpg"
exiftool "-TrackModifyDate=2024:03:16 22:20:01.102" "/mnt/d/por_organizar_de_cel_done/fotos/2024-03/IMG_20240316_222001_102.jpg"

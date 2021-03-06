#!/usr/bin/env python
import os
import sys


def moveto(file, target_folder):
    os.rename(''+directory+'/'+file, ''+target_folder+'/'+file)


directory = os.getcwd()
# target_pdf = directory+'/pdfs' PDFs are now moved to docs
target_mp3 = directory+'/Music'
target_vid = directory+'/Videos'  # Added videos
target_img = directory+'/Pictures'
target_zip = directory+'/Archives'  # renamed to archives to associate other formats e.g(zip, 7z, rar)
target_docs = directory+'/Documents'  # renamed to documents

#list of known formats here can be added
"""
All format lists were taken from wikipedia,
not all of them were added due to extensions not being
exclusive to one format such as webm, or raw
Audio - https://en.wikipedia.org/wiki/Audio_file_format
Images - https://en.wikipedia.org/wiki/Image_file_formats
Video - https://en.wikipedia.org/wiki/Video_file_format
Documents - https://en.wikipedia.org/wiki/List_of_Microsoft_Office_filename_extensions Majority of it is from MS Office
"""

image_formats = ['.png','.jpeg','.gif','.jpg','.bmp','.svg','webp']

audio_formats = ['.mp3','.aac','.flac','.ogg','.wma','.m4a','.aiff']

video_formats = ['.flv','.ogv','.avi','.mp4','.mpg','.mpeg','.3gp']

doc_formats = ['.pdf','.doc','.docx','.xls','.xlsv','.xlsx','.ppt','.pptx','.ppsx','.odp','.odt','.ods']

archive_formats = ['.rar','.zip','.7z','.tar.gz','.tar.bz2', '.tar']

images = []
audios = []
videos = []
docs = []
archives = []



print("Scanning Files")

if(len(sys.argv)==1):

    for file in os.listdir(directory):
        filename, file_ext = os.path.splitext(file)
        file_ext = file_ext.lower()

        if file_ext in audio_formats:
            audios.append(file)
        elif file_ext in video_formats:
            videos.append(file)
        elif file_ext in image_formats:
            images.append(file)
        elif file_ext in archive_formats:
            archives.append(file)
        elif file_ext in doc_formats:
            docs.append(file)

    if not os.path.exists(target_mp3) and len(audios) > 0:
        os.makedirs(target_mp3)
    if not os.path.exists(target_vid) and len(videos) > 0:
        os.makedirs(target_vid)
    if not os.path.exists(target_img) and len(images) > 0:
        os.makedirs(target_img)
    if not os.path.exists(target_zip) and len(archives) > 0:
        os.makedirs(target_zip)
    if not os.path.exists(target_docs) and len(docs) > 0:
        os.makedirs(target_docs)

    for file in audios:
        moveto(file, target_mp3)
    for file in videos:
        moveto(file, target_vid)
    for file in images:
        moveto(file, target_img)
    for file in archives:
        moveto(file, target_zip)
    for file in docs:
        moveto(file, docs)

    print("Done!")
else:
    formats = []
    #Arguments will be given like: classifier -s .py .pyc "Python Files"
    if(sys.argv[1]=='-s' or sys.argv[1]=='-S'):
        for argument in sys.argv[2:]:
            formats.append(argument)

            target_dir = directory+'/'+argument[1:]
            if not os.path.exists(target_dir):
                os.makedirs(target_dir)

        for file in os.listdir(directory):
            filename, file_ext = os.path.splitext(file)
            file_ext = file_ext.lower()
            if(file_ext in formats):
                moveto(file, target_dir)
        print("Done!")
    else:
        print("Invalid Option")

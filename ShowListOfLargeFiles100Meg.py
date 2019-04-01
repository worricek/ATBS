#! /usr/bin/python3
# Walk a dir tree and identify files with jpg or pdf copy these files to a new location

import os, sys

def fileExtSearch(folder,size):
    print(sys.argv[1])
    print(sys.argv[2])
#TODO walk the tree and check if extension is in basename
    for folderName, subfolders, filenames in os.walk(folder):
        for subfolder in subfolders:
            #Comment because this is being stoopid!
            #Another comment because this doesnt seem to be working!
            continue
        for filename in filenames:
            try:
                if os.path.getsize(os.path.join(folderName, filename))>size:
                    print(os.path.join(folderName, filename))
            except FileNotFoundError:
                print('File Not Found: '+filename)
fileExtSearch(sys.argv[1],int(sys.argv[2]))

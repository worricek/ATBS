#! /usr/local/python
# Walk a dir tree and identify files with jpg or pdf copy these files to a new location

import os, shutil

def fileExtSearch(folder,extension):
#TODO walk the tree and check if extension is in basename
    NewFolder='/home/worrall/Desktop/NewFolder'+str(extension).upper()
    if not os.path.exists(NewFolder):
        NewFolder='/home/worrall/Desktop/NewFolder'+str(extension).upper()
        NewFolder=os.makedirs('/home/worrall/Desktop/NewFolder'+str(extension).upper())
    else:
        print('Path Exists already!')
        NewFolder='/home/worrall/Desktop/NewFolder'+str(extension).upper()
    for folderName, subfolders, filenames in os.walk(folder):
        #absFolder=folderName
        print('')
        #print(subfolders)
        #print(filenames)
        
        for subfolder in subfolders:
            print('')
            #absFolder=os.path.join(folderName, subfolders)
        
        for filename in filenames:
            #print(folderName)
            if extension in filename:
                absFolder=os.path.join(folderName, filename)
                print(absFolder)
                #print('SUBFOLDER OF '+folderName+': '+subfolder)
                print('Filename "%s" found with extension "%s"...'%(absFolder, extension.upper()))
                #TODO Print this filename and copy to a new folder
                if filename in os.listdir(NewFolder):
                    print('File already copied, ignoring!')
                    continue
                print('Copying file to new folder: ...')
                shutil.copy(absFolder,NewFolder)

fileExtSearch('/home/worrall/Desktop','.py')

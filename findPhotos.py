#! /usr/local/python
# Walk a dir tree and identify files with jpg or pdf copy these files to a new location

import os, shutil
from PIL import Image

extList = ['.JPG', '.PNG']

def fileExtSearch(folder):
# walk the tree and check if extension is in basename
    #NewFolder=os.makedirs('/home/worrall/Desktop/NewPhotoFolder', exist_ok=True) # Photos in this folder on the desktop

    for folderName, subfolders, filenames in os.walk(folder):
        #absFolder=folderName
        #print('')
        #print(subfolders)
        #print(filenames)
        photoFolderList=[]
        switch = 'no'
        #print(folderName, subfolders, filenames)
        for subfolder in subfolders:
            print('')
            #absFolder=os.path.join(folderName, subfolders)
        
        for filename in filenames:
            fileCount=0
            #print(folderName)
            for file in filenames:
                f_name, f_ext = os.path.splitext(file)
                #print(folderName+'/'+file)
                if f_ext.upper() not in extList:
                    continue
                try:
                    im = Image.open(folderName+'/'+file)
                except FileNotFoundError:
                    print('Problem opening file ' + file)
                    continue
                if im.size[0] > 500 and im.size[1] > 500: #imWidth, imHeight = im.size
                    fileCount+=1
                    photoFolderList.append(os.path.join(folderName, file))
            #print(fileCount, len(filenames))
            if (fileCount/len(filenames)>0.5): 
                switch='yes'
                
        if switch == 'yes':
            print(folderName + ' is a photos folder!!!')
            #print('SUBFOLDER OF '+folderName+': '+subfolder)
                #The section below in comments is used in case you want to copy the files
                #as well as just indentify the folder
            '''
                for photoPath in photoFolderList:
                    if filename in os.listdir(NewFolder):
                        print('File already copied, ignoring!')
                        continue
                    print('Copying file ' + photoPath + ' to new folder: ...')
                    shutil.copy(photoPath,NewFolder)
            '''
fileExtSearch('/home/worrall/Desktop/photos')

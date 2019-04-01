#! /usr/local/python
#backuptozip.py copies an entire directory to a zip

import zipfile, os

def BackUpToZip(folder):
    folder=os.path.abspath(folder)
    print(folder)
    number=1
    
    while True:
        zipFileName=os.path.basename(folder)+'_'+str(number)+'.zip'
        print(zipFileName)
        if not os.path.exists(zipFileName):
            break
        number+=1
    print('Creating %s...' %(zipFileName))
    backupZip=zipfile.ZipFile(zipFileName,'w')
    
    for foldername,subfolders,filenames in os.walk(folder):
        print('Adding files in %s....' %(foldername))
        backupZip.write(foldername)
        for filename in filenames:
            newBase=os.path.basename(folder)+'_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            backupZip.write(os.path.join(foldername,filename))
    backupZip.close()
    print('Done')
        
BackUpToZip('/home/worrall/Downloads')

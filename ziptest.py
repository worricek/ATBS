import os,zipfile
os.chdir('/home/worrall/Desktop')

for file in os.listdir():
    try:
        filezip=zipfile.ZipFile(file)
        filezip.extractall()
        filezip.close()
    except zipfile.BadZipFile:
        print('not a zip')
        
        

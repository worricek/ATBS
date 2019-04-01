#! /usr/bin/python3

import zipfile, os, sys

if len(sys.argv)<2:
    print('Buddy....Now listen ......You need to enter the zip file name to so I can unzip stuff .......')
else:
    print('Zip file needs to be in <home dir>/Downloads')
    print('Unzipping Stuff ........')

    os.chdir('/home/worrall/Downloads')
    # move to the folder with the zip file

    filetoUnZip = zipfile.ZipFile(sys.argv[1])
    filetoUnZip.extractall() #unzip the stuff to the current working directory
    filetoUnZip.close()

    print('Unzipped the Stuff .........')

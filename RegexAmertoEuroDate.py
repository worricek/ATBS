#! /usr/local/python
# Renames files with American dates to Euro dates

import shutil, os, re 

datePattern=re.compile(r'''^(.*?) # all text before the date
                ((0|1)?\d)-                       # one or two digits for the month
                ((0|1|2|3)?\d)-                 # one or two digits for the day
                ((19|20)\d\d)                  # four digits for the year
                (.*?)$                             # all text after the date
                ''', re.VERBOSE)

for amerFilename in os.listdir('.'):
    mo=datePattern.search(amerFilename)
    if mo==None:
        continue
    beforepart=mo.group(1)
    monthpart=mo.group(2)
    daypart=mo.group(4)
    yearpart=mo.group(6)
    endpart=mo.group(8)
    euroFilename=beforepart+daypart+'-'+monthpart+'-'+yearpart+endpart
    absWorkingDir=os.path.abspath('.')
    amerFilename=os.path.join(absWorkingDir,amerFilename)
    euroFilename=os.path.join(absWorkingDir,euroFilename)
    print('Renaming "%s" to "%s"...' % (amerFilename,euroFilename))
    shutil.move(amerFilename,euroFilename)
    
    

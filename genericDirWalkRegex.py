import os

workingdir=input('Whats the folder you want to walk and regex ? ')
os.chdir(workingdir)
cwd=os.getcwd()
print(cwd)
for folderName, subfolders, filenames in os.walk('C:\\delicious'):
    print('The current folder is ' + folderName)
    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
            for filename in filenames:
                print('FILE INSIDE ' + folderName + ': '+ filename)
    print('')

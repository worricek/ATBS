#!/user/loca/python
import os,sys,re

while True:
#Search all txt files in the directory
#Ask the user for search string and perform regex on each txt file
#Ask the user what directoy to search on
    print('The current working directory is: ' + os.getcwd())
    dirinput=input("What dir would you like to search in? (Type 'current' to search current. Usage <dir,dir,dir>). Press <ENTER> to quit: ")
    if dirinput=="":
        break
    UserRegexInput=input('What would you like to search for? <ENTER> to exit: ')
    if UserRegexInput=="":
        break
    if dirinput=='current':
        dirinput=os.getcwd()
    else:
        NewDirRegex=re.compile(r'\s|,')
        NewDir=NewDirRegex.sub('/', dirinput)
        NewDir='/'+NewDir
        #print(NewDir)
        #Could not get this part to work. ie Converting a string to path
        #NewDirTest=os.path.split(dirinput)
        #print(NewDirTest)
        #NewDir=dirinput.join(os.path.split)
        #NewDir=os.path.join(os.path.sep, dirinput)
        #print(NewDir)
        if not os.path.exists(NewDir):
            print('Path does no exist!')
            break
        dirinput=os.chdir(NewDir)
        #print(dirinput)
    for filename in os.listdir(dirinput):
    #Check if file is a txt file and then open ane search for txt
        #print(filename)
        if 'txt' in filename:
            TxtFile=open(filename,'r')
            TxtFileContents=TxtFile.read()
            UserRegex=re.compile(UserRegexInput)
            RegexResults=UserRegex.findall(TxtFileContents)
            if not RegexResults==[]:
                print(filename + ' has the string ' + str(RegexResults))
            else:
                print(filename + ' is a txt file but does not contain ' + UserRegexInput)
            TxtFile.close()
        #else:
         #   print(filename + ' is not a txt file')
    repeat=input('Would you like to search again (y or n)? ')
    if repeat == 'n':
        break

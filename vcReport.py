#! /usr/bin/python3

import os, re

wd=os.chdir('/home/worrall/Downloads/cdr-UDC') #set working directory

participants=0 #Variable to show number of participants
vctotal=0 # Variable to show the number of VCs
vc='Audio Only: No' # If this string is not in the file then we are assuming it is audio only
vcoraudio='Audio Only: ' # Using this to count the number of unique participants
hours=0 
minutes=0
seconds=0
totalduration=0 # Variable used to tally up the total VC minutes
summfile=open('/home/worrall/VC Summary Report.txt',  'w') # Results file

#This is the regex we are searching for in each VC file. 
durationregex=re.compile(r'(Actual Duration:) (\d{2})(:)(\d{2})(:)(\d{2})')


print('Listing all VCs and the total VCs and participants below: \n')
summfile.write('Listing all VCs and the total VCs and participants below: \n')
summfile.write('\n')

#Loop thrpough each file in the directory
for filename in os.listdir(wd):
#    print(filename)
    duration='Actual Duration: ' # Reset the duration variable - just for printing
    file=open(filename, 'r') #Open the file
    filecontent=file.read() # Read its contents into a variable - as a string
    if vc in filecontent: # confirming if this is a vc or not 
        thisvc=0 #number of participants for this individual vc
        vctotal+=1 # Add this to the total number of vcs
        durationsearch=durationregex.search(filecontent) # search this file for the regex
        if durationsearch == None: #if you cant find it ignore this file and go to the next one
            continue
        hours=int(durationsearch.group(2))*60
        minutes=int(durationsearch.group(4))
        totalduration+=(hours+minutes)
#        print(totalduration)
        file.close() #close the file. get it ready for the line by line read. 
        file=open(filename,  'r') 
        for line in file.readlines(): #open the file again so we can read each line separately. 
            if vcoraudio in line: #this is to count the number of participants
                participants+=1
                thisvc+=1
            if duration in line: #assign the variable to the duration of the conference. 
                duration=line   
        if thisvc<2: #check if there was less than 2 participants and ignore if so
            participants-=1
            vctotal-=1
            totalduration-=(hours+minutes)
            continue
        #Print results to the screen and to the file defined above.
        print(filename + ' had ' + str(thisvc) + ' number of participants.')
        summfile.write(filename + ' had ' + str(thisvc) + ' number of participants.')    
        summfile.write('\n')
        print(duration + '\n')
        summfile.write(duration + '\n')
    file.close() #close each file after you open it. 
#   time.sleep(0.2)
#TODO Print out the total sum of VC's, participants and duration
totaldurationhours=totalduration/60 #work out the duration in hours. 
totaldurationhours=round(totaldurationhours, 2) # round it to 2 decimal places 

#Print summary to screen and write to the file defined above. 
print('\nTotal number of VCs: ' + str(vctotal))
summfile.write('\nTotal number of VCs: ' + str(vctotal))
summfile.write('\n')
print('Total number of participants in all VCs: ' + str(participants))
summfile.write('Total number of participants in all VCs: ' + str(participants) + '\n')
print('Total duration - minutes - of all VCs: '+ str(totalduration))
summfile.write('Total duration - minutes - of all VCs: '+ str(totalduration))
summfile.write('\n')
print('Total duration - hours - of all VCs: '+ str(totaldurationhours))
summfile.write('Total duration - hours - of all VCs: '+ str(totaldurationhours))
summfile.write('\n')
summfile.close() #close the file

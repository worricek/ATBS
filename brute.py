#! /usr/bin/python3

import PyPDF2

#Take the input of the PDF file you want to decrypt and open the dictionary
# TODO Create a progress bar

file=input('Whats the PDF file you want me to check?...')
dictionary=open('dictionary.txt', 'r')
dictionaryContent=dictionary.readlines()

#Create a list of all words in dictionary.txt
#Loop over the list and check if the word decrypts the PDF.
#          Check upper and lowercase.
#          If it does print out the password.

num=1
pdfReader = PyPDF2.PdfFileReader(file)

if pdfReader.isEncrypted:
    for line in dictionaryContent:
        
        if pdfReader.decrypt(line.strip())==1 or pdfReader.decrypt(line.lower().strip()) == 1:
            print('The password is ' +  line)
            break
        print(line.strip(), line.lower().strip())
else:
    print('The file ' + file + 'is not encrypted!)')
    #progress=((num/88000)*100)
    #if type(progress) == float:
        #continue
    #else:
    #print(str(progress) + '% complete.')
    #num+=1    
#Close the files.


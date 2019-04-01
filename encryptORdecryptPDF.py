#! /usr/bin/python3

''' This code takes 3 arguments on the command line:
  arg1 - Folder to target
  arg2 - mode. Either encrypt or decrypt.
  arg3 - password to encrypt or decrypt
  
  It then searches the directory for PDF files and either encrypts or 
  decrypts depending on what the user input. 
  After encrypting or decrypting, it will delete the source file.
  TODO I would like to code up the 2 functions so that encrypt and decrypt are just called 
  when need and not actually part of the code.
   TODO There is also a bug in this code where it appends _encrypt.pdf or _decrypt.pdf
   to the back of the filename. It continues to append. So you will have the situation
   where the filename can be _encrypted.pdf_decrypted.pdf_encrypted.pdf etc.
'''

import os,sys, PyPDF2, send2trash

def decrypt (file):
    #TODO Finish Decrypt function.
    print('Not dont yet!')

def encrypt (file):
    #TODO Finish Decrypt function.
    print('Not dont yet!')


wd=sys.argv[1]
#wd='/home/worrall/pdf'
os.chdir(wd)
mode=sys.argv[2]
#mode='d'
password=sys.argv[3]
#password='swordfish'

#TODO Walk the folders and find PDF files

pdfFiles = []

for folderName, subfolders, filenames in os.walk(wd):
    print('The current folder is ' + folderName)
    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)
        if filename.endswith('.pdf'):
            pdfFiles.append(filename)
    print('')

for filename in pdfFiles:
    pdfFile = open(filename, 'rb')
    
    if mode=='e':
        pdfReader = PyPDF2.PdfFileReader(pdfFile)
        
        if pdfReader.isEncrypted == True:
            print('File ' + filename + ' is already encrypted, skipping ...')
            continue
            
        pdfWriter = PyPDF2.PdfFileWriter()
    
        for pageNum in range(pdfReader.numPages):
            pdfWriter.addPage(pdfReader.getPage(pageNum))
    
        pdfWriter.encrypt(password)
        resultFile=filename+'_encrypted.pdf'
        resultPdf = open(resultFile, 'wb')
        pdfWriter.write(resultPdf)
        resultPdf.close()    
        
        pdfReaderTest = PyPDF2.PdfFileReader(resultFile)
                
        if pdfReaderTest.decrypt(password)==1:
            print('File to be deleted is ' + filename)
            send2trash.send2trash(filename)
        else:
            print('Something went wrong, the file ' + filename + ' did not get encrypted properly!')        
    else:
        pdfReader = PyPDF2.PdfFileReader(pdfFile)
        
        if pdfReader.isEncrypted != True:
            print('File ...' + filename + ' could not be decrypted as its not encrypted!')
            continue   
        if pdfReader.decrypt(password)==0:
            print('File ...' + filename + ' could not be decrypted. Wrong password!')
            continue
        else:
            pdfWriter = PyPDF2.PdfFileWriter()
    
            for pageNum in range(pdfReader.numPages):
                pdfWriter.addPage(pdfReader.getPage(pageNum))
    
            pdfReader.decrypt(password)
            resultPdf = open(filename + '_decrypted.pdf',  'wb')
            pdfWriter.write(resultPdf)
            resultPdf.close()
            if pdfReader.decrypt(password)==1:
                print('File ' + filename + ' sent to trash!')
                send2trash.send2trash(filename)
         
            print('File ...' + filename + ' has been decrypted!')


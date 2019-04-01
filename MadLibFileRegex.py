#! /usr/local/python

import re

#Function to Open a txt file in read only and print contents
Madlibfile=open('madlibfile.txt', 'r')
OriginalText=Madlibfile.read()
print(OriginalText)

#Take input on adjective, noun, adverb and verb
Adjective=input('Enter adjective: ')
Noun=input('Enter noun: ')
Adverb=input('Enter adverb: ')
Verb=input('Enter noun: ')

#Perform a regex search and replace for each of the items in the text file
Adjresults=re.compile(r'ADJECTIVE')
Nounresults=re.compile(r'NOUN')
Advresults=re.compile(r'ADVERB')
Verbresults=re.compile(r'VERB')
Stage1ADJ=Adjresults.sub(Adjective, OriginalText)
Stage2NOUN=Nounresults.sub(Noun,Stage1ADJ)
Stage3ADV=Advresults.sub(Adverb,Stage2NOUN)
FinalStage=Verbresults.sub(Verb,Stage3ADV)

#And save as a new txt file
NewFile=open('NewFile.txt', 'w')
NewFile.write(FinalStage)
NewFile.close()

#Print this file to the screen
NewFile=open('NewFile.txt', 'r')
NewFileContents=NewFile.read()
print(NewFile.read())
NewFile.close()
Madlibfile.close()


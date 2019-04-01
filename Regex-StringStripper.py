#! /usr/bin/python3

import re

def StripCharacters(StripThisString, WithThisString):
    if WithThisString == '':
        StripRegexL=re.compile(r'^\s+')
        StripRegexR=re.compile(r'\s+$')
        NewString=StripRegexL.sub("", StripThisString)
        FinalString=StripRegexR.sub("", NewString)
        print(FinalString, end="")
    else:
        WithThisString='['+WithThisString+']'
        CurlyWhirly=re.sub(WithThisString,'', StripThisString)
        print(CurlyWhirly)
 
ThingToStrip=input('Enter the string to strip: ')
StripItWithThis=input('Enter what you want to remove. Enter Nothing to remove leading and trailing spaces: ')
StripCharacters(ThingToStrip, StripItWithThis)

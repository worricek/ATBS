#! /usr/bin/python3

import re

def stripRegex(x,string):

    if x == '':
        spaceLeft = re.compile(r'^\s+')
        stringLeft = spaceLeft.sub('',string)
        spaceRight = re.compile(r'\s+$')
        stringRight = spaceRight.sub('',string)
        stringBoth = spaceRight.sub('',stringLeft)
        print(stringLeft)
        print(stringRight)

    else:
        charLeft = re.compile(r'^(%s)+'%x)
        stringLeft = charLeft.sub('',string)
        charRight = re.compile(r'(%s)+$'%x)
        stringBoth = charRight.sub('',stringLeft)
    print(stringBoth)

x1 = ''
x2 = 'Spam'
x3 = 'pSam'
string1 = '      Hello world!!!   '
string2 = 'SpamSpamBaconSpamEggsSpamSpam'
stripRegex(x1,string1)
stripRegex(x2,string2)
stripRegex(x3,string2)

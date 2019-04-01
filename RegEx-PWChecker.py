#! /usr/bin/python3

import re

while True:
    PW=input('Enter Password (Must be upper lower and number : ')
    if re.match(r'([a-zA-Z0-9]){8,}', PW):    
        break
    else:
        print('Password does not match complexity requirements')

#Result=PasswordRegEx.findall(PW)
#if Result==None:
#    print('Test')
 #   print(PasswordRegEx)
#print(Result.group())

#If Result == None:
 #   Print('Not complex')
#else:
 #   Print('Yep')
    
    



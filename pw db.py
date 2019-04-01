#! /usr/bin/python3
# An insecure password manager program
import sys, pyperclip

Password={'gmail':'stuff','facebook':'things','wireless':'andstuff'}

if len (sys.argv) < 2:
    print ('Usage: pw db.py [account] - copy account password')
    sys.exit()
    
account=sys.argv[1]     #1st command line argument is the password
if account in Password:
    pyperclip.copy(Password[account])
    print('Password for ' + account + ' copied to clipboard')
else:
    print('There is no account of this name in the DB')


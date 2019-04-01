import pyzmail
import subprocess
import smtplib
import imapclient
import implib
import getpass

#from . import exceptions

#file=open('commandFile.txt', 'w')
#Open email account and find emails from me.

commandList = []
password = 'xxxx'
emailLogin = input ('Enter your email login -> ')
searchFrom = input('What email addresses do you want to search from -> ')
emailTo = input('Enter the email address you want to be notified at -> ')
emailFrom = input('Enter the email address you want to send from -> ')
errorFile = open('commandErrFile.txt', 'w')

implib._MAXLINE=10000000
imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
pw=getpass.getpass(prompt='Enter your email password -> ')

#Handle the login error
while True:
    try:
        imapObj.login(emailLogin, pw)
        smtpObj.login(emailLogin,pw)
        break
    except:
        print('Invalid Username or Password Try again ....')

imapObj.select_folder('INBOX', readonly=False)
UIDs = imapObj.search(['FROM', emailSearch])
#print(UIDs)
foundElements=[]
for emailAddr in UIDs:
    rawMessages = imapObj.fetch(emailAddr,  ['BODY[]', 'FLAGS'])
    message = pyzmail.PyzMessage.factory(rawMessages[emailAddr][b'BODY[]'])    
    if message.text_part == None:
        continue
    #file.write(str(message))
    message=message.text_part.get_payload().decode(message.text_part.charset)

#If the email is from me check for a password in the body and if there 
# execute the rest of it as a sub process

    if password in message:
        commandFound=message.split(',')[0]
        print("Command found!!!" + commandFound)
        #print(commandFound)
        commandList.append(commandFound)
        imapObj.delete_messages(emailAddr)
        imapObj.expunge()
        continue


# Wait for the subprocess to end before killing the app
# Log to a file to check later
# Email or text me that the job is done

for command in commandList:
    try:
        commandProc = subprocess.Popen(command) 
        commandProc.wait()
        if commandProc.poll() == 0:
            errorFile.write(command + ' this command ran successfully!\n')
            smtpObj.sendmail(emailFrom,emailTo,command + \
            ' has completed. Check the commandErrFile for details')
        else:
            errorFile.write(command + ' this command had a problem and did not complete successfully\n')
    except Exception as e:
        errorFile.write(command + ' did not run as there was an error: ' + str(e) + '\n')
        #print(command + 'did not run as there was an error: ' + str(e))
    
errorFile.close()
smtpObj.quit()
imapObj.logout()

import smtplib, random,  shelve
#To do : Store the chores so that next weeks chores are not the same as last weeks
#To do: schedule the chorelist weekly

receivers=['someAddr','someOtherAddr']
chores=['table','dishes', 'dishwasher', 'compost', 'feed dog', 'recycling']

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
pw=input()
lg=input()
emailTo=input()
emailFrom=input()

smtpObj.login(lg,pw)


for emailAddr in receivers:
    print(emailAddr)
    receiverList=[]
    for i in range (1, 4):
        randomChore=random.choice(chores)
        receiverList.append(randomChore)
        chores.remove(randomChore) # this chore is now taken, so remove it
        print(randomChore)
    print(receiverList)
#    shelfFile=shelve.open('choreFile')
  #  shelfFile[emailAddr]=str(receiverList)
  #  print(shelfFile[emailAddr])
    smtpObj.sendmail(emailFrom,emailTo,str(receiverList))

#shelfFile.close()
smtpObj.quit()

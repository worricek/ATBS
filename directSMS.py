# smsAuth

import requests, bs4

def SMS(message):
    #Get the SMS authentication details and mobile
    
    file=open('smsAuth', 'r')
    fileContent=file.read()
    auth=fileContent.split()
    username = auth[0]
    password = auth[1]
    mobile = auth[2]
    
    #Get the directSMS website and html in prep for getting the connection ID
    
    url='http://api.directsms.com.au/s3/http/connect?username=%s&password=%s' % (username, password)
    res	=	requests.get(url)
    res.raise_for_status()
    soup	=	bs4.BeautifulSoup(res.text)
   
    #	Find	the connection ID in prep for sending the message
    
    htmlElem=soup.select('p')
    idElem=htmlElem[0].getText()
    id=idElem.split()[1]
    print(id)
    
    #Send the message 
    
    url='http://api.directsms.com.au/s3/http/send_message?connectionid=%s \
    &message=%s&senderid=directSMS&to=%s&type=1-way' % (id, message, mobile)
    res	=	requests.get(url)
    res.raise_for_status()

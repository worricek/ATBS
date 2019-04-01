#! /usr/bin/python

# Write	a	program	that	takes	an	email	address	and	string	of	text	on	the	command	line	and
#then,	using	Selenium,	logs	into	your	email	account	and	sends	an	email	of	the	string	to	the
#provided	address.	(You	might	want	to	set	up	a	separate	email	account	for	this	program.)
#This	would	be	a	nice	way	to	add	a	notification	feature	to	your	programs.	You	could	also
#write	a	similar	program	to	send	messages	from	a	Facebook	or	Twitter	account.

from selenium import webdriver
import sys
import time
import getpass

#TODO take command line arguments and create an email address and a string of txt
while True:
    if len(sys.argv)<2:
        print('Provide an email address and text of email address to send')
    else:
        email = sys.argv[1]
        print(email)
        emailcontent=" ".join(sys.argv[2:])
        print(emailcontent)
        break

emailLogin=input('Enter Email address login: ')
senderPassword=getpass.getpass("Enter your password: ")

#TODO login to email account
browser	=	webdriver.Chrome()
browser.get('http://gmail.com')
emailElem	=	browser.find_element_by_id('identifierId')
emailElem.send_keys(emailLogin)
nextElem	=	browser.find_element_by_id('identifierNext')
nextElem.click()
time.sleep(5)
passwordElem	=	browser.find_element_by_name('password')
passwordElem.send_keys(senderPassword)
passwordElem	=	browser.find_element_by_id('passwordNext')
passwordElem.click()
time.sleep(10)

#TODO send an email to the email address provided
composeElem	=	browser.find_element_by_css_selector('div.z0')
composeElem.click()
time.sleep(5)

recipientElem = browser.find_element_by_id(':13u')
recipientElem.send_keys(email)
time.sleep(5)

subjectElem = browser.find_element_by_id(':13c')
subjectElem.send_keys('Automated Email from Selenium')
time.sleep(5)

contentElem = browser.find_element_by_id(':14h')
contentElem.send_keys(emailcontent)
time.sleep(5)

sendElem = browser.find_element_by_id(':132')
sendElem.click()
time.sleep(5)

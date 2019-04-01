#! /usr/local/python

# Write	a	program	that	takes	an	email	address	and	string	of	text	on	the	command	line	and
#then,	using	Selenium,	logs	into	your	email	account	and	sends	an	email	of	the	string	to	the
#provided	address.	(You	might	want	to	set	up	a	separate	email	account	for	this	program.)
#This	would	be	a	nice	way	to	add	a	notification	feature	to	your	programs.	You	could	also
#write	a	similar	program	to	send	messages	from	a	Facebook	or	Twitter	account.

from selenium import webdriver
import sys

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

#TODO login to email account
webbrowser.open('https://www.google.com/maps/place/'+address)


#TODO send an email to the email address provided


browser=webdriver.Chrome()
#browser.get('http://inventwithpython.com')
#linkElem	=	browser.find_element_by_link_text('Cracking Codes with Python')
#linkElem.click()	#	follows	the	"Read	It	Online"	link
#try:
#    elem=browser.find_element_by_class_name('dropdown-item')
#    print('Found <%s> element with that class name!' % (elem.tag_name))
#except:
#    print('No tag of that name')
browser.get('https://www.outsourcing.optus.net.au/eFRAMS3/')
emailElem	=	browser.find_element_by_name('user')
emailElem.send_keys('voiceandvideo')
passwordElem	=	browser.find_element_by_name('pass')
passwordElem.send_keys('asicservicedesk')
passwordElem.submit()    
menu	=	browser.find_elements_by_id("el7")
#passwordElem= browser.move_to_element(passwordElem)
#passwordElem.perform()
hover = ActionChains(browser).move_to_element(menu)
hover.perform()
passwordElem	=	browser.find_element_by_name('download')
passwordElem.click()

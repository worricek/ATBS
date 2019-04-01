#!	python3
#	downloadXkcd.py	-	Downloads	every	single	XKCD	comic.

from selenium import webdriver
#from selenium.webdriver.common.action_chains import ActionChains
import requests,  os,  bs4
    
    #	TODO:	Find	the	URL	of	the	comic	image.
    comicElem	=	soup.select('#comic	img')
    if	comicElem	==	[]:
        print('Could	not	find	comic	image.')
    else:
        #comicUrl	=	comicElem[0].get('src')
        comicUrl='http:'+comicElem[0].get('src')
        print(comicUrl)
        print(comicElem)
        #	TODO:	Download	the	image.
        print('Downloading	image	%s...'	%	comicUrl)
        res	=	requests.get(comicUrl)
        res.raise_for_status()
        
    #	TODO:	Save	the	image	to	./xkcd.
        imageFile	=	open(os.path.join('xkcd',	os.path.basename(comicUrl)),	'wb')
        for	chunk	in	res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
    #	TODO:	Get	the	Prev	button's	url
    prevLink	=	soup.select('a[rel="prev"]')[0]
    url	=	'http://xkcd.com'	+	prevLink.get('href')
    
print('Done.')


browser=webdriver.Chrome()
browser.get('https://www.outsourcing.optus.net.au/eFRAMS3/')
emailElem	=	browser.find_element_by_name('user')
emailElem.send_keys('voiceandvideo')
passwordElem	=	browser.find_element_by_name('pass')
passwordElem.send_keys('asicservicedesk')
passwordElem.submit()    
#menuElem	=	browser.find_elements_by_id("el7")
#hover = ActionChains(browser).move_to_element(menuElem)
#hover.perform()
#passwordElem	=	browser.find_element_by_name('download')
#passwordElem.click()



payload = {'inUserName': 'VOICEANDVIDEO','inUserPass': 'ASICSERVICEDESK'}
with requests.Session() as s:
    p = s.post('https://www.outsourcing.optus.net.au/eFRAMS3/', data=payload)
    print p.text
url	=	'https://www.outsourcing.optus.net.au/eFRAMS3/'			#	starting	url
requests.post(url, data=payload)
os.makedirs('eFrams',	exist_ok=True)			#	store	Files in eFrams directory
url	=	'https://www.outsourcing.optus.net.au/eFRAMS3/controller.html?action=home
res	=	requests.get(url)
res.raise_for_status()
soup	=	bs4.BeautifulSoup(res.text)
docElem	=	soup.select('a')
print(docElem)
#while	True:
    #	TODO:	Download	the	files.
 #   print('Downloading	page	%s...'	%	url)
 #   res	=	requests.get(url)
 #   res.raise_for_status()
    
    soup	=	bs4.BeautifulSoup(res.text)


From StackOverflow:
    import requests

# Fill in your details here to be posted to the login form.
payload = {
    'inUserName': 'username',
    'inUserPass': 'password'
}

# Use 'with' to ensure the session context is closed after use.
with requests.Session() as s:
    p = s.post('LOGIN_URL', data=payload)
    # print the html returned or something more intelligent to see if it's a successful login page.
    print p.text

    # An authorised request.
    r = s.get('A protected web page url')
    print r.text
        # etc...

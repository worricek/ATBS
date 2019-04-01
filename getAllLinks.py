#! /usr/bin/python

#Write a program that, given the URL of a web page, will attempt to download every linked
#page on the page. The program should flag any pages that have a 404 “Not Found” status
#code and print them out as broken links.

import requests,  bs4

url='https://packetpushers.net/archives/'
print('Searching...' + url + ' for new news')	
res	=	requests.get(url)
res.raise_for_status()

soup	=	bs4.BeautifulSoup(res.text)

linkElems	=	soup.select('link')
linkNumber=len(linkElems)-1
for	i	in	range(linkNumber):
    url=(linkElems[i].get('href'))
    try:
        res	=	requests.get(url)
        print(url)
    except requests.exceptions.RequestException as e:
        print(e)
 

#! /usr/bin/python

#Write	a	program	that	goes	to	a	photo-sharing	site	like	Flickr	or	Imgur,	searches	for	a
#category	of	photos,	and	then	downloads	all	the	resulting	images.	You	could	write	a
#program	that	works	with	any	photo	site	that	has	a	search	feature.

import requests,  bs4, sys,  webbrowser

print('Searching...')	#	display	text	while	searching the Image site
url='https://https://imgur.com/search?q='	+	'	'.join(sys.argv[1:])
print(url)
res	=	requests.get(url)
res.raise_for_status()

#	Retrieve	top	search	result	links.
soup	=	bs4.BeautifulSoup(res.text)

#	Open	a	browser	tab	for	each	result.
linkElems	=	soup.select('.image-list-link')
print(linkElems)

#numOpen	=	min(5,	len(linkElems))
#for	i	in	range(numOpen):
 #   webbrowser.open('http://google.com'	+	linkElems[i].get('href'))
    

#! /usr/bin/python

#Write	a	program	that	goes	to	a	photo-sharing	site	like	Flickr	or	Imgur,	searches	for	a
#category	of	photos,	and	then	downloads	all	the	resulting	images.	You	could	write	a
#program	that	works	with	any	photo	site	that	has	a	search	feature.

import requests,  bs4

url='https://packetpushers.net/archives/'
print('Searching...' + url + ' for new news')	
res	=	requests.get(url)
res.raise_for_status()

soup	=	bs4.BeautifulSoup(res.text)

linkElems	=	soup.select('.entry-content a')
docNumber=len(linkElems)-1
for	i	in	range(docNumber):
    try:
        playFile	=	open('PP-News.txt',	'r')
    except FileNotFoundError:
        print("File Does not exist. Creating 'PP-News.txt'")
        playFile =open('PP-News.txt','w')
        playFile.close()
        playFile	=	open('PP-News.txt',	'r')
    playFilecontents=playFile.read()
    url=(linkElems[i].get('href'))
    res	=	requests.get(url)
    res.raise_for_status()
    soup	=	bs4.BeautifulSoup(res.text)
    titleElems	=	soup.select('.entry-title')
    if str(titleElems[0].getText()) in playFilecontents:
            print('Skipping news item: ' + titleElems[0].getText())
            playFile.close()
            continue
    else:
        playFile.close()
        playFile=open('PP-News.txt','a')
        textElems = soup.select('.entry-content p')
        playFile.write('\n' + titleElems[0].getText() + '\n')
        paraNumber=len(textElems)-1
        for paragraph in range(paraNumber):
            playFile.write('\n' + textElems[paragraph].getText() + '\n')
        playFile.close()




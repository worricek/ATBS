#!	python3
#	downloadXkcd.py	-	Downloads	every	single	XKCD	comic.

import requests,  os,  bs4,  time

url	=	'http://xkcd.com'														#	starting	url
os.makedirs('xkcd',	exist_ok=True)			#	store	comics	in	./xkcd
startTime=time.time()

while	not	url.endswith('#'):
    #	Download	the	page.
    # print('Downloading	page	%s...'	%	url)
    res	=	requests.get(url)
    res.raise_for_status()
    
    soup	=	bs4.BeautifulSoup(res.text)
    
    #	Find	the	URL	of	the	comic	image.
    comicElem	=	soup.select('#comic	img')
    if	comicElem	==	[]:
        print('Could	not	find	comic	image.')
    else:
        #comicUrl	=	comicElem[0].get('src')
        comicUrl='http:'+comicElem[0].get('src')
        #print(comicUrl)
        #print(comicElem)
        #print(os.path.basename(comicUrl))
        #print(os.listdir('xkcd'))
        if "http://" in comicUrl:      
            if os.path.basename(comicUrl) not in os.listdir('xkcd'):        #	Download	the	image.
                print('Downloading	image	%s...'	%	comicUrl)
                res	=	requests.get(comicUrl)
                res.raise_for_status()
        
    #	Save	the	image	to	./xkcd.
                imageFile	=	open(os.path.join('xkcd',	os.path.basename(comicUrl)),	'wb')
                for	chunk	in	res.iter_content(100000):
                    imageFile.write(chunk)
                imageFile.close()
            else:
                print('Already have	image	%s...'	%	os.path.basename(comicUrl))
    #	Get	the	Prev	button's	url
    prevLink	=	soup.select('a[rel="prev"]')[0]
    url	=	'http://xkcd.com'	+	prevLink.get('href')
endTime=time.time()
print('Done.')
print('Took %s seconds to complete.' %(endTime-startTime))

#!	python3
#	downloadXkcd.py	-	Downloads	every	single	XKCD	comic.

import requests,  os,  bs4,  time

url	=	'http://www.lefthandedtoons.com'														#	starting	url
os.makedirs('lht',	exist_ok=True)			#	store	comics	in	./xkcd
startTime=time.time()

while	not	url.endswith('#'):
    #	Download	the	page.
    # print('Downloading	page	%s...'	%	url)
    res	=	requests.get(url)
    res.raise_for_status()
    
    soup	=	bs4.BeautifulSoup(res.text)
    
    #	Find	the	URL	of	the	comic	image.
    comicElem	=	soup.select('.comicimage')
    if	comicElem	==	[]:
        print('Could	not	find	comic	image.')
    else:
        #comicUrl	=	comicElem[0].get('src')
        comicUrl=comicElem[0].get('src')
        #comicUrl='stuffandthings'
        #print(comicUrl)
        #print(comicElem)
        #print(os.path.basename(comicUrl))
        #print(os.listdir('xkcd'))
        if "http://" in comicUrl:      
            if os.path.basename(comicUrl) not in os.listdir('lht'):        #	Download	the	image.
                print('Downloading	image	%s...'	%	comicUrl)
                res	=	requests.get(comicUrl)
                res.raise_for_status()
        
    #	Save	the	image	to	./xkcd.
                imageFile	=	open(os.path.join('lht',	os.path.basename(comicUrl)),	'wb')
                for	chunk	in	res.iter_content(100000):
                    imageFile.write(chunk)
                imageFile.close()
            else:
                print('Already have	image	%s...'	%	os.path.basename(comicUrl))
    #	Get	the	Prev	button's	url
    prevLink=soup.select('.prev a')[0]
    url	=	'http://www.lefthandedtoons.com'	+	prevLink.get('href')
endTime=time.time()
print('Done.')
print('Took %s seconds to complete.' %(endTime-startTime))

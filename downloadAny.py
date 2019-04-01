#!	python3
#	downloadXkcd.py	-	Downloads	every	single	XKCD	comic.

import requests,  os,  bs4,  time

startTime=time.time()

urlDict = {'xkcd':'http://xkcd.com', 'lht':'http://www.lefthandedtoons.com'}
soupValues = {'lht':'.comicimage', 'xkcd':'#comic	img'}
prevLinkValues = {'lht':'.prev a', 'xkcd':'a[rel="prev"]'}

for k, v in urlDict.items():
    os.makedirs(k,	exist_ok=True)			#	store	comics	in	key ./directory 
    url=v
    print(v)
    while	not	url.endswith('#'):
    #	Download	the	page.
    # print('Downloading	page	%s...'	%	url)
        res	=	requests.get(url)
        res.raise_for_status()
        
        soup	=	bs4.BeautifulSoup(res.text)
    
    #	Find	the	URL	of	the	comic	image.
        comicElem	=	soup.select(soupValues[k])
        print(comicElem)
        if comicElem == []:
            print('Nothing found')
        else:
            comicUrl=comicElem[0].get('src')
            print(comicUrl)
            if "//imgs" in comicUrl:
                comicUrl = 'http:'+comicUrl
                print(comicUrl)
            if "http://" in comicUrl:      
                if os.path.basename(comicUrl) not in os.listdir(k):        #	Download	the	image.
                    res	=	requests.get(comicUrl)
                    res.raise_for_status()
    #	Save	the	image	to	./xkcd.
                    print('Downloading	image	%s...'	%	comicUrl)
                
                    imageFile	=	open(os.path.join(k,	os.path.basename(comicUrl)),	'wb')
                    for	chunk	in	res.iter_content(100000):
                        imageFile.write(chunk)
                        imageFile.close()
                else:
                    print('Already have	image	%s...'	%	os.path.basename(comicUrl))
    #	Get	the	Prev	button's	url
            prevLink=soup.select(prevLinkValues[k])[0]
            url	=	v+prevLink.get('href')
            print(url)

endTime=time.time()
print('Done.')
print('Took %s seconds to complete.' %(endTime-startTime))

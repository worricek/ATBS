#!	python3
#	downloadXkcd.py	-	Downloads	every	single	XKCD	comic.

import requests,  os,  bs4,  time

url	=	'http://buttersafe.com'														#	starting	url
os.makedirs('BS',	exist_ok=True)			#	store	comics	in	./xkcd
startTime=time.time()

while	not	url.endswith('#'):
    #	Download	the	page.
    # print('Downloading	page	%s...'	%	url)
    res	=	requests.get(url)
    res.raise_for_status()
        
    soup	=	bs4.BeautifulSoup(res.text)
    
    #	Find	the	URL	of	the	comic	image.
    comicElem	=	soup.select('#comic img')
    comicUrl=comicElem[0].get('src')
    #comicUrl	=	comicElem[0].get('href')
    print(comicElem)
    print(comicUrl)
    #comicUrl=comicElem[0].get('src')
    if	comicElem	==	[]:
        print('Could	not	find	comic	image.')
    else:
        #comicUrl	=	comicElem[0].get('href')
        #comicUrl=comicElem[0].get('src')
        #comicUrl='stuffandthings'
        #print(comicUrl)
        #print(comicElem)
        #print(os.path.basename(comicUrl))
        #print(os.listdir('xkcd'))
        if "http://" in comicUrl:      
            #res	=	requests.get(comicUrl)
            #res.raise_for_status()
            #comicElem	=	soup.select('#comic img')
            #print(comicUrl)
            #print(comicElem[0].get('src'))
            #comicUrl=comicElem[0].get('src')
            #print(comicUrl)
            #print(comicElem)
            if os.path.basename(comicUrl) not in os.listdir('BS'):        #	Download	the	image.
                res	=	requests.get(comicUrl)
                res.raise_for_status()
    #	Save	the	image	to	./xkcd.
                print('Downloading	image	%s...'	%	comicUrl)
                
                imageFile	=	open(os.path.join('BS',	os.path.basename(comicUrl)),	'wb')
                for	chunk	in	res.iter_content(100000):
                    imageFile.write(chunk)
                imageFile.close()
            else:
                print('Already have	image	%s...'	%	os.path.basename(comicUrl))
    #	Get	the	Prev	button's	url
    prevLink=soup.select('#headernav a')[0]
    url	=	url+prevLink.get('href')
    print(url)
endTime=time.time()
print('Done.')
print('Took %s seconds to complete.' %(endTime-startTime))

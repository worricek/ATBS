#!	python3
#	downloadXkcd.py	-	Downloads	every	single	XKCD	comic.

import requests,  os,  bs4,  time,  threading

startTime=time.time()

urlDict = {'xkcd':'http://xkcd.com/', 'lht':'http://www.lefthandedtoons.com/'}
soupValues = {'lht':'.comicimage', 'xkcd':'#comic	img'}
#prevLinkValues = {'lht':'.prev a', 'xkcd':'a[rel="prev"]'}

def downloadAny(startComic, endComic):

    for k, v in urlDict.items():
        os.makedirs(k,	exist_ok=True)			#	store	comics	in	key ./directory 
        url=v
        #print(v)

        for urlNumber in range(startComic, endComic):
    #	Download	the	page.
    # print('Downloading	page	%s...'	%	url)
            res = requests.get(url + '%s' % (urlNumber))            
            try:
                res.raise_for_status()
            except Exception as exc:
                print('There was a problem: %s' % (exc))

            soup	=	bs4.BeautifulSoup(res.text)
    
    #	Find	the	URL	of	the	comic	image.
            comicElem	=	soup.select(soupValues[k])
            #print(comicElem)
            if comicElem == []:
                print('Nothing found')
            else:
                comicUrl=comicElem[0].get('src')
                #print(comicUrl)
                #if "//imgs" in comicUrl:
                    #comicUrl = 'http:'+comicUrl
                    #print(comicUrl)
                #if "http://" in comicUrl:      
                if os.path.basename(comicUrl) not in os.listdir(k):        #	Download	the	image.
                    res	=	requests.get(comicUrl)
                    res.raise_for_status()
    #	Save	the	image	to	./xkcd.
                    print('Downloading	image	%s...'	%	comicUrl)
                
                    imageFile	=	open(os.path.join('/home/worrall/Desktop',	os.path.basename(comicUrl)),	'wb')
                    for	chunk	in	res.iter_content(100000):
                        imageFile.write(chunk)
                        imageFile.close()
                else:
                    print('Already have	image	%s...'	%	os.path.basename(comicUrl))
    #	Get	the	Prev	button's	url
                #prevLink=soup.select(prevLinkValues[k])[0]
                #url	=	v+prevLink.get('href')
                #print(url)

downloadThreads = []
# a list of all the Thread objects
for i in range(1, 1400, 100):
# loops 14 times, creates 14 threads
    downloadThread = threading.Thread(target=downloadAny, args=(i, i + 99))
    downloadThreads.append(downloadThread)
    downloadThread.start()
    
# Wait for all threads to end.
for downloadThread in downloadThreads:
    downloadThread.join()
    print('Done.')

endTime=time.time()
print('Done.')
print('Took %s seconds to complete.' %(endTime-startTime))

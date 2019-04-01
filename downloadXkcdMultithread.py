#!	python3
#	downloadXkcd.py	-	Downloads	every	single	XKCD	comic.

import requests,  os,  bs4,  time,  threading

url	=	'http://xkcd.com'														#	starting	url

startTime=time.time()

os.makedirs('xkcd', exist_ok=True) # store comics in ./xkcd

def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
# Download the page.
        #print('Downloading page http://xkcd.com/%s...' % (urlNumber))
        res = requests.get('http://xkcd.com/%s' % (urlNumber))
        try:
            res.raise_for_status()
        except Exception as exc:
            print('There was a problem: %s' % (exc))
        soup = bs4.BeautifulSoup(res.text)
# Find the URL of the comic image.
        comicElem = soup.select('#comic img')
        if comicElem == []:
            print('Could not find comic image.')
        else:
            comicUrl = 'http:' + comicElem[0].get('src')
            if os.path.basename(comicUrl) not in os.listdir('xkcd'):        
                #	Download	the	image.
                print('Downloading image %s...' % (comicUrl))
                res = requests.get(comicUrl)
                res.raise_for_status()
# Save the image to ./xkcd.
                imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
                for chunk in res.iter_content(100000):
                    imageFile.write(chunk)
                imageFile.close()
            else:
                print('Already have	image	%s...'	%	os.path.basename(comicUrl))
# Create and start the Thread objects.
downloadThreads = []
# a list of all the Thread objects
for i in range(1, 1400, 100):
# loops 14 times, creates 14 threads
    downloadThread = threading.Thread(target=downloadXkcd, args=(i, i + 99))
    downloadThreads.append(downloadThread)
    downloadThread.start()
    
# Wait for all threads to end.
for downloadThread in downloadThreads:
    downloadThread.join()
    print('Done.')

endTime=time.time()
print('Took %s seconds to complete.' %(endTime-startTime))

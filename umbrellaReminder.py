# Code that checks the weather forecast and sends an SMS if its going to rain.
# Uses custom code library directSMS with the input being the message.

import requests,bs4, json, directSMS

message = 'Grab the brolly!'

# Get the html from the Weather website for Kellyville

url = 'http://api.openweathermap.org/data/2.5/forecast?q=%s&APPID=%s' % ('kellyville,au','some API key')
res	=	requests.get(url)
res.raise_for_status()
soup	=	bs4.BeautifulSoup(res.text)

# Get the weather element - in json - from the html

linkElems	=	soup.select('p')
jsonData=json.loads(linkElems[0].getText())
weatherData=jsonData['list']

# If rain iss forecast call directSMS and send a message

if 'rain'  in weatherData[39]['weather'][0]['description']:
    directSMS.SMS(message)

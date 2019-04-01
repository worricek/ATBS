#! python3
# quickWeather.py - Prints the weather for a location from the command line.
import json, requests, sys
# Compute location from command line arguments.
#if len(sys.argv) < 2:
#    print('Usage: quickWeather.py location')
#sys.exit()
#location = ' '.join(sys.argv[1:])
stuff=['kellyville', 'nsw']
location=''.join(stuff)
# Download the JSON data from OpenWeatherMap.org's API.
#url ='http://api.openweathermap.org/data/2.5/weather?q=%s&APPID=3a312e942230769b31cd5387500984ff' % (location)
url='http://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=3a312e942230769b31cd5387500984ff'
response = requests.get(url)
response.raise_for_status()

# Load JSON data into a Python variable.
weatherData = json.loads(response.text)
print(response.text)

# Print weather descriptions.

w = weatherData['list']
print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])

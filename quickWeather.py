#! python3
# quickWeather.py - Prints the weather for a location from the command line.
#
# This code is part of a list of corrections on reddit at:
# https://www.reddit.com/r/inventwithpython/comments/8ykq1i/automate_the_boring_stuff_with_python_corrections/
# -/u/JoseALerma
# DW Comments: This code would not work with sending the APIKEY to the function.
# which is bad coding. But the results of the GET was 401 client error not authorised. 
# Modified by only sending location to the function but i have left the full code in for 
# reference.
 
import json, requests, sys, shelve, datetime
 
 
def getWeather(loc):
#def getWeather(loc, apikey):
    # Download the JSON data from OpenWeatherMap.org's API.
    #url = '3a312e942230769b31cd5387500984ff' % (loc)
    url = 'http://api.openweathermap.org/data/2.5/forecast?q=%s&APPID=%s' % (loc,'3a312e942230769b31cd5387500984ff')
    response = requests.get(url)
    response.raise_for_status()
 
    # Load JSON data into a Python variable.
    data = json.loads(response.text)
 
    now = datetime.datetime.now(tz=datetime.timezone.utc)
    data["savedTime"] = now
    print(data)
    return data
 
 
# Compute location from command line arguments.
if len(sys.argv) < 2:
    print('Usage: P05_quickWeather.py city,country code')
    sys.exit()
location = ' '.join(sys.argv[1:])
 
# Get API Key from file
with open("apikey.txt") as file:
    apiKey = file.read()

# Open shelf to read data
weatherShelf = shelve.open("weather")
#print(weatherShelf["Data"])
print(weatherShelf) 
# Download and save data to shelf
#location='sydney,au'
if not list(weatherShelf.keys()):  # Shelf empty, download data
    #weatherShelf["data"] = getWeather(location, apiKey)
    weatherShelf["data"] = getWeather(location)

else:
    # Check for 10 minute interval between API requests
    timeNow = datetime.datetime.now(tz=datetime.timezone.utc)
    savedTime = weatherShelf["data"]["savedTime"]
    timedelta = timeNow - savedTime
    interval = datetime.timedelta(minutes=10)
    if timedelta < interval:
        city = weatherShelf["data"]["city"]
        print("RequestError: Need to wait %s minutes. Using saved data for: %s, %s" %
              (round((interval - timedelta).total_seconds()/60, 2), city["name"], city["country"]))
    else:
        #weatherShelf["data"] = getWeather(location, apiKey)
        weatherShelf["data"] = getWeather(location)
 
# Print weather descriptions
w = weatherShelf["data"]['list']
print(w)
count = int(weatherShelf["data"]["cnt"])
print(count)

# Print current weather
currentDate = datetime.datetime.strptime(w[0]["dt_txt"][:10], '%Y-%m-%d')
print('Current weather in %s:' % location)
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
tomorrowDate = currentDate + datetime.timedelta(days=1)
dayAfterDate = currentDate + datetime.timedelta(days=2)
print()
 
for i in range(1, count):
    currentDate = datetime.datetime.strptime(w[i]["dt_txt"][:10], '%Y-%m-%d')
    # If current date is greater than tomorrow date, print tomorrow weather
    if currentDate > tomorrowDate:
        print('Tomorrow:')
        print(w[i]['weather'][0]['main'], '-', w[i]['weather'][0]['description'])
        tomorrowDate = currentDate + datetime.timedelta(days=7)  # past the 5-day forecast
        print()
    # If current date is greater than day after date, print day after tomorrow weather
    elif currentDate > dayAfterDate:
        print('Day after tomorrow:')
        print(w[i]['weather'][0]['main'], '-', w[i]['weather'][0]['description'])
        break
 
weatherShelf.close()

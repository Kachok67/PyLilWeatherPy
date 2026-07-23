try:
    import json
    from urllib.request import urlopen
    from urllib.error import URLError
    import os
    import threading
    import time
    import UI
except ImportError:
    Error = "There was an error importing the libraries"

Error = ""


usroption = input("Would you like to set custom latitude and longtitude? (y/n for Vienna) ")
if usroption == "y":
    latitude = input("Please enter a latitude: ")
    longtitude = input("Please enter a longtitude: ")
else:
    latitude = 48.20849
    longtitude = 16.37208

def CheckErrors():
    while True:
        if not Error == "":
            print(Error)
            os._exit(1)
            exit()
        time.sleep(0.1)

ErrorThread = threading.Thread(target=CheckErrors)
ErrorThread.start()

url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longtitude}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"

try:
    response = urlopen(url).read().decode()
except URLError:
    Error = "Data couldnt be fetched. Check your internet connection"

try:
    if not response == None:
        data = json.loads(response)
    else: Error = "There was no response from the url"
except json.JSONDecodeError:
    Error = "There was an error decoding the json"

with open("log", "w") as logfile:
    json.dump(data, logfile, indent=3)

try:
    print(f"The current temperature is {data['current']['temperature_2m']} Celcius")
    print(f"The current wind speed is {data['current']['wind_speed_10m']} km/h")
    print(f"The current time is {data['current']['time']}")

    currenttimeText = f"The current time is {data['current']['time']}"
    tempText = f"The current temperature is {data['current']['temperature_2m']} Celcius"
    windspeedText = f"The current wind speed is {data['current']['wind_speed_10m']} km/h"

    temps = data["hourly"]["temperature_2m"]

    print(f"Today's highest: {max(temps)}°C")
    print(f"Today's lowest: {min(temps)}°C")

    highestTempText = f"Todays highest temperature is {max(temps)}°C"
    lowestTempText = f"Todays lowest temperature is {min(temps)}°C"


    winds = data["hourly"]["wind_speed_10m"]
    print(f"Strongest wind today: {max(winds)} km/h")

    strongestWind = f"Strongest wind today: {max(winds)} km/h"

    # weather_code = data["current"]["relative_humidity_2m"]

    # if weather_code in [51, 53, 55, 61, 63, 65, 80, 81, 82]:
    #     print("It is raining")
    # else:
    #     print("No rain")

    
except KeyError:
    Error = "Some expected fields are missing in the json"



ui = UI.UI()
ui.CreateUI(latitude, longtitude, currenttimeText, tempText, highestTempText, lowestTempText, windspeedText, strongestWind)
ui.update()
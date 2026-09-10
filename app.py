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


# Font sizes
PfontSize = 12;
HfontSize = 16;
P2fontSize = 10;

# Asks user if they would like to use the default Vienna preset or enter custom coordinates
usroption = input("Would you like to set custom latitude and longtitude? (y/n for Vienna) ")
if usroption == "y":
    # Prompts the user to enter custom values
    latitude = input("Please enter a latitude: ")
    longtitude = input("Please enter a longtitude: ")
else:
    # Defaults
    latitude = 48.20849
    longtitude = 16.37208

# Error Checking subprocess (Checks every 200 Milliseconds to minimize perfomance impact)
def CheckErrors():
    while True:
        global Error  
        if not Error == "":
            print(Error)
            os._exit(1)
            exit()
        time.sleep(0.2)

# Initialises and starts the error checking process
ErrorThread = threading.Thread(target=CheckErrors)
ErrorThread.start()

# Url to fetch Jason from
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longtitude}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"

try:
    response = urlopen(url).read().decode()

# Probably a internet connection problem
except URLError:
    Error = "Data couldnt be fetched. Check your internet connection"

try:
    if not response == None:
        data = json.loads(response)
    else: Error = "There was no response from the url"
except json.JSONDecodeError:
    Error = "There was an error decoding the json"

# Logs...
with open("log", "w") as logfile:
    json.dump(data, logfile, indent=3)

try:
    # sets variables and prints data into terminal
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

    # Humidity (todo)
    # weather_code = data["current"]["relative_humidity_2m"]

    # if weather_code in [51, 53, 55, 61, 63, 65, 80, 81, 82]:
    #     print("It is raining")
    # else:
    #     print("No rain")
 
except KeyError:
    Error = "Some expected fields are missing in the json"


# Creates UI and Object
ui = UI.UI()
ui.CreateUI(latitude, longtitude, currenttimeText, tempText, highestTempText, lowestTempText, windspeedText, strongestWind ,PfontSize, HfontSize, P2fontSize)
ui.update()

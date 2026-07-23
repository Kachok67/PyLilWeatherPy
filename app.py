try:
    import json
    from urllib.request import urlopen
    from urllib.error import URLError
    import os
    import threading
    import time
    import tkinter
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

if os.path.exists("MyWeatherPy/log"):
    os.remove("MyWeatherPy/log")
    print("Log file has sucessfully been rewritten")

with open("MyWeatherPy/log", "w") as logfile:
    if not logfile == None:
        json.dump(data, logfile, indent=3)
    else:
        Error = "Logfile has not been found and couldnt be created"

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

class UI:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry("300x300")
        self.root.title("MyWeatherPy")
        self.root.configure(bg="#181818")
        self.root.attributes("-alpha", 0.9)


    def update(self):
        self.root.mainloop()

    def CreateUI(self):

        h1 = tkinter.Label(self.root, text="Current Weather in Vienna", font=("Depixel", 14), bg="#181818")
        h2 = tkinter.Label(self.root, text=f"({latitude},{longtitude})", font=("Depixel", 8), bg="#181818")

        if latitude == 48.20849 and longtitude == 16.37208:
            h1.config(text="Current Weather in Vienna")
        else: 
            h1.config(text="Current Weather")


        h1.pack()
        h2.pack()


        currenttimeLabel = tkinter.Label(self.root, text=currenttimeText + "\n", font=("Depixel", 10), bg="#181818")
        currenttimeLabel.pack()

        tempLabel = tkinter.Label(self.root, text=tempText, font=("Depixel", 10), bg="#181818")
        tempLabel.pack()

        maxtempLabel = tkinter.Label(self.root, text=highestTempText, font=("Depixel", 10), bg="#181818")
        maxtempLabel.pack()

        lowestTempLabel = tkinter.Label(self.root, text=lowestTempText + "\n", font=("Depixel", 10), bg="#181818")
        lowestTempLabel.pack()

        windspeedLabel = tkinter.Label(self.root,text=windspeedText, font=("Depixel", 10), bg="#181818")
        windspeedLabel.pack()

        maxwindspeedLabel = tkinter.Label(self.root,text=strongestWind, font=("Depixel", 10), bg="#181818")
        maxwindspeedLabel.pack()
ui = UI()
ui.CreateUI()
ui.update()
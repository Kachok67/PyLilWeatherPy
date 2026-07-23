import tkinter

class UI:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry("300x300")
        self.root.title("MyWeatherPy")
        self.root.configure(bg="#181818")
        self.root.attributes("-alpha", 0.9)

    def update(self):
        self.root.mainloop()

    def CreateUI(self, latitude, longtitude, currenttimeText, tempText, highestTempText, lowestTempText, windspeedText, strongestWind):

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

        windspeedLabel = tkinter.Label(self.root, text=windspeedText, font=("Depixel", 10), bg="#181818")
        windspeedLabel.pack()

        maxwindspeedLabel = tkinter.Label(self.root, text=strongestWind, font=("Depixel", 10), bg="#181818")
        maxwindspeedLabel.pack()
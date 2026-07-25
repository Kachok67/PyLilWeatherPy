import tkinter

class UI:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry("400x300")
        self.root.title("MyWeatherPy")
        self.root.configure(bg="#181818")
        self.root.attributes("-alpha", 0.9)

    def update(self):
        self.root.mainloop()

    def CreateUI(self, latitude, longtitude, currenttimeText, tempText, highestTempText, lowestTempText, windspeedText, strongestWind, PfontSize=12, HfontSize=16, P2fontSize=10):

        h1 = tkinter.Label(self.root, text="Current Weather in Vienna", font=("Depixel", 14), bg="#181818")
        h2 = tkinter.Label(self.root, text=f"({latitude},{longtitude})", font=("Depixel", 8), bg="#181818")

        if latitude == 48.20849 and longtitude == 16.37208:
            h1.config(text="Current Weather in Vienna")
        else:
            h1.config(text="Current Weather")

        h1.pack(pady=10, padx=10)
        h2.pack()

        currenttimeLabel = tkinter.Label(self.root, text=currenttimeText + "\n", font=("Depixel", PfontSize), bg="#181818")
        currenttimeLabel.pack()

        tempLabel = tkinter.Label(self.root, text=tempText, font=("Depixel", PfontSize), bg="#181818")
        tempLabel.pack()

        maxtempLabel = tkinter.Label(self.root, text=highestTempText, font=("Depixel", P2fontSize), bg="#181818")
        maxtempLabel.pack()

        lowestTempLabel = tkinter.Label(self.root, text=lowestTempText + "\n", font=("Depixel", P2fontSize), bg="#181818")
        lowestTempLabel.pack()

        windspeedLabel = tkinter.Label(self.root, text=windspeedText, font=("Depixel", PfontSize), bg="#181818")
        windspeedLabel.pack()

        maxwindspeedLabel = tkinter.Label(self.root, text=strongestWind, font=("Depixel", P2fontSize), bg="#181818")
        maxwindspeedLabel.pack()
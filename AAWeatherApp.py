
import tkinter as tk
import requests

API_key = '99e521a6cc75dfd9b2ef0b32bdb98341'

window = tk.Tk()
window.title("Anthony's Amazing Wether App")

canvas1 = tk.Canvas(window, width=400, height=300)
canvas1.pack()

label = tk.Label(window, text="Enter a city to see it's weather: ")
label.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label)    

entry= tk.Entry(window)
canvas1.create_window(200, 100, window=entry)

def deg_to_dir(num):
    val=int((num/22.5)+.5)
    arr=["N","NNE","NE","ENE","E","ESE", "SE", "SSE","S","SSW","SW","WSW","W","WNW","NW","NNW"]
    return arr[(val % 16)]

def get_weather():
    location = entry.get()

    weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid='
    final_url = weather_url + API_key
    weather_data= requests.get(final_url).json()
   
    weather_summary = weather_data['weather'][0]['description']
    temp = round(((weather_data['main']['temp'])-273.15)*9/5 + 32, 0) 
    wind = round(weather_data['wind']['speed'] * 2.237, 0)
    winddir = deg_to_dir(weather_data['wind']['deg'])

    canvas1.create_window(200, 100, window=entry)

    label3 = tk.Label(window, text= f'The current weather in {location} is {weather_summary}.',font=('helvetica', 9))
    canvas1.create_window(200, 230, window=label3)

    label4 = tk.Label(window, text= f'The current temperature is {temp:.0f}°F.',font=('helvetica', 9))
    canvas1.create_window(200, 250, window=label4)

    label5 = tk.Label(window, text= f'The wind is {wind:.0f} MPH out of the {winddir}.',font=('helvetica', 9))
    canvas1.create_window(200, 270, window=label5)

button = tk.Button(text='Go!', command=get_weather)
canvas1.create_window(200, 180, window=button)


window.mainloop()



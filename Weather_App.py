import requests
import json
import pyttsx3

city = input("Enter the name of the city\n")

url = f"https://api.weatherapi.com/v1/current.json?key=6c4e8cc58cc94bb5ae201555230511&q={city}"

r = requests.get(url)

# print(r.text)
weather_dic = json.loads(r.text)
country = weather_dic["location"]["country"]
temp = weather_dic["current"]["temp_c"]
wind = weather_dic["current"]["wind_kph"]
humidity = weather_dic["current"]["humidity"]
pressure = weather_dic["current"]["pressure_mb"]
cloud = weather_dic["current"]["cloud"]
feelslike = weather_dic["current"]["feelslike_c"]
precip = weather_dic["current"]["precip_mm"]
uv = weather_dic["current"]["uv"]

weather_info = f"'The location of {city} is in {country}  , termperature is {temp} degree celcius , wind is {wind} kilometer per hour , humidity is {humidity} , pressure is {pressure} mb , cloud is {cloud} , feelslike {feelslike} , preciption is {precip} and UV index is {uv}' "

print(weather_info)

command = pyttsx3.init()
command.say(weather_info)
command.runAndWait()
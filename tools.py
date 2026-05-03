import requests
from config import WEATHER_API_KEY

def get_weather(city : str):

    URL= f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"    
    res = requests.get(URL).json()

    if res.get("main"):
        temp = res["main"]["temp"]
        desc = res["weather"][0]["description"]

        return f"city : {city}, temperature : {temp} degree C, description : {desc}"
    else:
        return "City Not Found"




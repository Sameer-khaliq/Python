# #Challenge 1 — Load and verify .env works

# from dotenv import load_dotenv
# import os
# load_dotenv()

# key = os.environ.get('WEATHER_API_KEY')
# city = os.environ.get('CITY')

# if key:
#     print(f"Key found: {key[:5]}")
#     print(f"City: {city}")


#Challenge 2 — Fetch live weather data
from dotenv import load_dotenv
import os
import requests

load_dotenv()
KEY = os.environ.get("WEATHER_API_KEY")
cities = ['Gujrat', 'Lahore', 'Islamabad', 'Karachi']
metrics = os.environ.get('UNITS','metric')

if not KEY:
    print("No key found!!")
else:
    url = "https://api.openweathermap.org/data/2.5/weather"
for city in cities:
    params = {
        "q" : city,
        "appid": KEY,
        "units": metrics
    }

    response = requests.get(url, params= params)
    
    if response.status_code == 200:
        data = response.json()
        print(f"===========Weather of {city}============\n")
        print(f"City: {data['name']}")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Feels like: {data['main']['feels_like']}°C")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Weather: {data['weather'][0]['description']}")
        print(f"Wind speed: {data['wind']['speed']} m/s\n")

    elif response.status_code == 401:
        print("Invalid API key — check your .env")
    elif response.status_code == 404:
        print(f"City '{city}' not found")
    else:
        print(f"Error: {response.status_code}")

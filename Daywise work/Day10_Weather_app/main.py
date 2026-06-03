from dotenv import load_dotenv
import os
import requests

load_dotenv()

KEY = os.environ.get("WEATHER_API_KEY")
UNITS = os.environ.get("UNITS", "metric")
cities = ["Gujrat", "Lahore", "Islamabad", "Karachi"]

if not KEY:
    print("No key found!! Check your .env file")
else:
    url = "https://api.openweathermap.org/data/2.5/weather"

    for city in cities:
        params = {
            "q": city,
            "appid": KEY,
            "units": UNITS
        }

        try:
            response = requests.get(url, params=params)

            if response.status_code == 200:
                data = response.json()
                print(f"=========== Weather of {city} ============\n")
                print(f"City:        {data['name']}")
                print(f"Temperature: {data['main']['temp']}°C")
                print(f"Feels like:  {data['main']['feels_like']}°C")
                print(f"Humidity:    {data['main']['humidity']}%")
                print(f"Weather:     {data['weather'][0]['description']}")
                print(f"Wind speed:  {data['wind']['speed']} m/s\n")

            elif response.status_code == 401:
                print(f"Invalid API key — check your .env")
            elif response.status_code == 404:
                print(f"City '{city}' not found")
            else:
                print(f"Error {response.status_code} for {city}")

        except requests.exceptions.ConnectionError:
            print(f"Network error — could not reach API for {city}")
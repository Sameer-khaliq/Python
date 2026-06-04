# Weather App

A Python command-line app that fetches real-time weather data
using the OpenWeatherMap API.

## Features
- Fetches live weather for any city
- Displays temperature, humidity, wind speed, and conditions
- Handles invalid cities and network errors gracefully
- Supports multiple cities in one run

## Tech Stack
- Python 3.x
- requests library
- python-dotenv
- OpenWeatherMap API

## Setup

### 1. Clone the repo
git clone https://github.com/yourusername/weather-app.git
cd weather-app

### 2. Create virtual environment
python -m venv venv
source venv/bin/activate

### 3. Install dependencies
pip install -r requirements.txt

### 4. Set up environment variables
Create a .env file in the root folder:
WEATHER_API_KEY=your_openweathermap_key_here
UNITS=metric

### 5. Run the app
python main.py

## Example Output
City:        Gujrat
Temperature: 32°C
Feels like:  36°C
Humidity:    65%
Weather:     hazy sunshine
Wind speed:  3.2 m/s


## Author
Sameer — AI Developer Roadmap Day 10
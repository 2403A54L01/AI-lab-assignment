import requests

def get_weather(city):
    # SECURITY RISK: API Key is hardcoded and visible!
    api_key = "12345_SECRET_KEY" 
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    response = requests.get(url)
    return response.json()

print(get_weather("Hyderabad"))

import os

def get_weather_secure(city):
    # SECURE: Fetches key from environment variables
    api_key = os.environ.get("WEATHER_API_KEY")
    if not api_key:
        raise ValueError("No API Key found")
    
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    response = requests.get(url)
    return response.json()
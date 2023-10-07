# Author: Emmanuella Solomon
# Date: 07/10/23
# Description: Handles API calls and all info relating to the API

import requests
import os
from dotenv import load_dotenv

#load env variables
load_dotenv()

# Retrieve the API key from an environment variable
api_key = os.getenv('OPENWEATHERMAP_API_KEY')

def fetch_weather_data():
    if not api_key:
        print('Error: API key not found in environment variables')
        exit(1)

    # Define the base URL for the OpenWeatherMap API
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'

    # Specify the location you want to get weather data for (e.g., city name and country code)
    location = 'London,uk'

    # Create the complete API URL
    complete_url = f'{base_url}q={location}&appid={api_key}'

    # Send an HTTP GET request to the API
    response = requests.get(complete_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response and return weather data as a dictionary
        data = response.json()
        temperature = data['main']['temp']
        weather_description = data['weather'][0]['description']
        return {'temperature': temperature, 'description': weather_description}
    else:
        print('Error: Unable to retrieve weather data')
        return None
    

# Example usage:
if __name__ == "__main__":
    weather_data = fetch_weather_data()
    if weather_data:
        print(f'Temperature: {weather_data["temperature"]} K')
        print(f'Weather Description: {weather_data["description"]}')


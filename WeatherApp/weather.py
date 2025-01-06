import requests #this module is used to hit the API and get the info
from dotenv import load_dotenv #to fetch the API key
import os
import pprint

load_dotenv()

def get_current_weather():
    print("*****Weather Application*****")

    city_name = input("\nEnter the name of the City: ")

    request_url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={os.getenv("API_KEY")}&units=metric'

    #print(request_url)
    weather_data = requests.get(request_url).json()
    
    #print(weather_data)
    print(f'\n The temperature in {city_name} is {weather_data["main"]["temp"]:.1f}°')

get_current_weather()

#created the dev branch
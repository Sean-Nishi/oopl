"""
Sean Nishi
10/21/2021
Homework 3 get_weather.py
Program prompts user for city, retrieves data from website,
then displays said data with a Weather Parser
"""

from weather_parser import WeatherParser
import requests
from requests.exceptions import HTTPError

def display_weather_summary(raw_file):
	"""Takes a jsonFile, creates a WeatherParser,
	then displays all conditions"""
	try:
		current_conditions_parser = WeatherParser(raw_file)
		#display conditions
		current_conditions_parser.get_weather_description()
		current_conditions_parser.get_feels_like_f()
		current_conditions_parser.get_cloud_cover()
		current_conditions_parser.get_sunrise()
		current_conditions_parser.get_sunset()
	except:
		print(f"Error: Could not create a WeatherParser with input json file")

#Main Program
print(f"Weather Checker App Starting...\n"\
	f"Welcome. Ready to get your local weather report.")

city_name = input(f"Please enter your city: ")

URL = f"https://wttr.in/" + city_name + f"?format=j1"

try:
	#request file
	raw_file = requests.get(URL)
	#confirm we got the file
	raw_file.raise_for_status()

	display_weather_summary(raw_file)

except HTTPError as http_error:
        print(f'HTTP error occurred: {http_error}')
except Exception as error:
    print(f'Other error occurred: {error}')

#Sean Nishi
#10/14/2021
#Homework 3 Weather App
#weather_parser.py

class WeatherParser:
	"""Weather Parser class. Takes a raw JSON file, converts it to JSON,
	and has public methods to retrieve data."""

	def __init__(self, jsonFile):
		"""Initializes the json file, will be a dictionary"""
		self._currentConditions = jsonFile.json()

	def get_feels_like_f(self):
		"""retrieves 'FeelsLikeF' element from JSON String"""
		print(f"Feels like (F): "\
			f"{self._currentConditions['current_condition'][0]['FeelsLikeF']}")
		return self._currentConditions['current_condition'][0]['FeelsLikeF']

	def get_cloud_cover(self):
		"""retrieves 'cloudcover' element from JSON String"""
		print(f"Cloud Cover: "\
			f"{self._currentConditions['current_condition'][0]['cloudcover']}")
		return self._currentConditions['current_condition'][0]['cloudcover']

	def get_weather_description(self):
		"""retrieves 'weatherDesc' element from JSON String"""
		print(f"Weather Description: "\
			f"{self._currentConditions['current_condition'][0]['weatherDesc'][0]['value']}")
		return self._currentConditions['current_condition'][0]['weatherDesc'][0]['value']

	def get_sunset(self):
		"""retrieves 'sunset' element from JSON String"""
		print(f"Sunset: "\
			f"{self._currentConditions['weather'][0]['astronomy'][0]['sunset']}")
		return self._currentConditions['weather'][0]['astronomy'][0]['sunset']

	def get_sunrise(self):
		"""retrieves 'sunrise' element from JSON String"""
		print(f"Sunrise: "\
			f"{self._currentConditions['weather'][0]['astronomy'][0]['sunrise']}")
		return self._currentConditions['weather'][0]['astronomy'][0]['sunrise']
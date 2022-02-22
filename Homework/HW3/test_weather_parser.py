#Sean Nishi
#10/14/2021
#Homework 3 test_weather_parser.py

import unittest
import requests
from weather_parser import *

class TestWeatherParser(unittest.TestCase):
	"""Tests for a 'weather_parser'"""

	def setUp(self):
		"""sets up the weather_parser class with fresh data from URL"""
		URL = f"https://wttr.in/Boston?format=j1"
		raw_file = requests.get(URL)
		self._jsonFile = raw_file.json()
		self._conditions = WeatherParser(raw_file)
		#print(f"{URL}")
	
	def test_get_feels_like_f(self):
		"""Can we retrieve 'feels_like_f' element?"""
		feels_like_f = self._conditions.get_feels_like_f()
		#what do they return? Null? False? void?
		self.assertIsInstance(feels_like_f, str)
		self.assertIsNotNone(feels_like_f)

	def test_get_cloud_cover(self):
		"""Testing get_cloud_cover method"""
		cloud_cover = self._conditions.get_cloud_cover()
		self.assertIsInstance(cloud_cover, str)
		self.assertIsNotNone(cloud_cover)

	def test_get_weather_description(self):
		"""Testing get_weather_description method"""
		weather_desc = self._conditions.get_weather_description()
		self.assertIsInstance(weather_desc, str)
		self.assertIsNotNone(weather_desc)

	def test_get_sunset(self):
		"""Testing get_sunset method"""
		sunset = self._conditions.get_sunset()
		self.assertIsInstance(sunset, str)
		self.assertIsNotNone(sunset)

	def test_get_sunrise(self):
		"""testing get_sunrise method"""
		sunrise = self._conditions.get_sunrise()
		self.assertIsInstance(sunrise, str)
		self.assertIsNotNone(sunrise)

if __name__ == '__main__':
	unittest.main()
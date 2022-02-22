"""
Sean Nishi
Homework 4
10/29/2021
settings.py
"""

class Settings:
	"""A class to store all settings for Rock Game."""

	def __init__(self):
		"""Initializes the game's settings."""
		#Screen settings
		self.screen_width = 600
		self.screen_height = 400
		self.background_color = (255, 0, 255)

		#Player settings
		self.player_speed = .6#.25
		self.starting_lives = 1

		#Rock settings
		self.rock_speed = .25
		self.max_rocks = 50
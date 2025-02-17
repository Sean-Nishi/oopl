"""
Sean Nishi
Homework 4
10/29/2021
"""

import pygame
from pygame.sprite import Sprite

class Player(Sprite):
	"""Class for the player"""

	def __init__(self, rock_game):
		"""Initialize the player and set its starting position."""
		super().__init__()
		self.screen = rock_game.screen
		self.settings = rock_game.settings
		self.screen_rect = rock_game.screen.get_rect()

		#Load the player image and get its rect
		self.image = pygame.image.load('images/player.bmp')
		self.rect = self.image.get_rect()

		#Start the player in the middle of the scren
		self.rect.center = self.screen_rect.center

		#Store a decimal value for the player's horizontal position
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

		#Movement flags
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False

	def update(self):
		"""Update the player's position based on movement flags."""
		#Update player's x values

		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.player_speed
		if self.moving_left and self.rect.left > 0:
			self.x -= self.settings.player_speed
		#Update player's y values
		if self.moving_up and self.rect.top > 0:
			self.y -= self.settings.player_speed
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.y += self.settings.player_speed

		#Update rect object from player's coords
		self.rect.x = self.x
		self.rect.y = self.y

	def blitme(self):
		"""Draw the player at its current location."""
		self.screen.blit(self.image, self.rect)

	def center_player(self):
		"""Center the player on the screen"""
		self.rect.center = self.screen_rect.center_player
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)
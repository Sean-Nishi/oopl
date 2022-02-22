"""
Sean Nishi
Homework 4
10/29/2021
"""

import pygame
import random
from datetime import datetime
from pygame.sprite import Sprite

class Rock(Sprite):
	"""Class for a rock"""
	#static directionals to help with rock behavior
	sides = ['top', 'bottom', 'left', 'right']
	move_directions = ['down', 'up', 'right', 'left']
	#seed the spawning of the rocks
	random.seed(datetime.now())

	def __init__(self, rock_game):
		"""Initialize the rock."""
		super().__init__()
		self.screen = rock_game.screen
		self.settings = rock_game.settings
		self.screen_rect = rock_game.screen.get_rect()

		#Load rock image and set its rect attributes
		self.image = pygame.image.load('images/rock.bmp')
		self.rect = self.image.get_rect()

		#Start each new rock at a random position on the border of the screen
		side = random.choice(self.sides)
		#spawns a rock ON the screen
		#spawn rock on top of screen randomly between left and right
		if side == 'top':
			self.rect.x = random.randrange(0, self.screen_rect.right - self.rect.right, 1)
			self.rect.y = 0 - self.rect.right#self.screen_rect.top
			self.move_direction = self.move_directions[0]
		#spawn rock on bottom of screen randomly between left and right
		elif side == 'bottom':
			self.rect.x = random.randrange(0, self.screen_rect.right - self.rect.right, 1)
			self.rect.y = self.screen_rect.bottom
			self.move_direction = self.move_directions[1]
		#spawn rock on left side of screen randomly between top and bottom
		elif side == 'left':
			self.rect.x = self.screen_rect.left - self.rect.right
			self.rect.y = random.randrange(0, self.screen_rect.bottom - self.rect.bottom, 1)
			self.move_direction = self.move_directions[2]
		#spawn rock on right side of screen randomly between top and bottom
		elif side == 'right':
			self.rect.x = self.screen_rect.right
			self.rect.y = random.randrange(0, self.screen_rect.bottom - self.rect.bottom, 1)
			self.move_direction = self.move_directions[3]

		#Store the rock's exact position
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

	def at_edge(self):
		"""Returns True if rock is at edge of screen."""
		screen_rect = self.screen.get_rect()
		#Depends on which direction the rock is moving
		if self.move_direction == 'down':
			#if moving down, if top of sprite is below screen return true
			if self.rect.y > screen_rect.bottom:
				return True
		if self.move_direction == 'up':
			if self.rect.y < screen_rect.top:
				return True
		if self.move_direction == 'left':
			if self.rect.x < screen_rect.left:#screen_rect.right?
				return True
		if self.move_direction == 'right':
			if self.rect.x > screen_rect.right:
				return True
		return False

	def update(self):
		"""Move the rock towards its respective position."""
		if self.move_direction == 'down':
			self.y += self.settings.rock_speed
			self.rect.y = self.y
		elif self.move_direction == 'up':
			self.y -= self.settings.rock_speed
			self.rect.y = self.y
		elif self.move_direction == 'right':
			self.x += self.settings.rock_speed
			self.rect.x = self.x
		elif self.move_direction == 'left':
			self.x -= self.settings.rock_speed
			self.rect.x = self.x

#TODO ending rock on left or top screen doesnt go past screen

"""
Sean Nishi
Homework 4
"""

import sys

import pygame
import time
from settings import Settings
from game_stats import GameStats
from player import Player
from rock import Rock

class MyGame:
	"""Overall class to manage game assets and behavior."""
	def __init__(self):
		"""Initializes the game, and create game resources."""
		pygame.init()
		#import the settings
		self.settings = Settings()

		#create display from the settings
		self.screen = pygame.display.set_mode(
			(self.settings.screen_width, self.settings.screen_height))
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height
		pygame.display.set_caption("Dodge The Rock!")

		#Create an instance to store game statistics
		self.stats = GameStats(self)
		
		#Create player as a single group (for collision detection)
		self.player = pygame.sprite.GroupSingle(Player(self))

		#Create initial rocks
		self.rocks = pygame.sprite.Group()
		self.rock_count = 0
		while(self.rock_count < self.settings.max_rocks):
			self._create_rock()

		#Create a timer variable for scoring
		self.font = pygame.font.SysFont(None, 32)
		self.start_time = pygame.time.get_ticks()
		self.timer_text = self.font.render(str(0), 1, (0, 0, 0))
		#timer displayed in topleft of screen
		self.timer_rect = self.timer_text.get_rect(topleft = self.screen.get_rect().topleft)

		#scoring + checking high score vars
		self.game_ended = False
		self.session_score = 0
		self.game_over_text = self.font.render("Game Over!", 1, (0, 0, 0))
		self.game_over_rect = self.game_over_text.get_rect(center = self.screen.get_rect().center)

	def run_game(self):
		"""Start the main loop for the game."""
		while True:
			#check for input
			self._check_events()
			#check if we need to spawn more rocks
			while self.rock_count <= self.settings.max_rocks:
				self._create_rock()

			#If we haven't died
			if self.stats.game_active:
				#update player
				self.player.update()
				#update rocks
				self._update_rocks()

			#update screen
			self._update_screen()

	def _check_events(self):
		"""Respond to keypresses and mouse events."""
		for event in pygame.event.get():
			#if the game is ended, can only quit
			if not self.stats.game_active:
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type == pygame.KEYUP:
					self._check_keyup_events(event)
			else:
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type == pygame.KEYDOWN:
					self._check_keydown_events(event)
				elif event.type == pygame.KEYUP:
					self._check_keyup_events(event)

	def _check_keydown_events(self, event):
		"""Respond to key presses."""
		if event.key == pygame.K_RIGHT:
			self.player.sprite.moving_right = True
		elif event.key == pygame.K_LEFT:
			self.player.sprite.moving_left = True
		elif event.key == pygame.K_UP:
			self.player.sprite.moving_up = True
		elif event.key == pygame.K_DOWN:
			self.player.sprite.moving_down = True

	def _check_keyup_events(self, event):
		"""Respond to key releases."""
		if event.key == pygame.K_RIGHT:
			self.player.sprite.moving_right = False
		if event.key == pygame.K_LEFT:
			self.player.sprite.moving_left = False
		if event.key == pygame.K_UP:
			self.player.sprite.moving_up = False
		if event.key == pygame.K_DOWN:
			self.player.sprite.moving_down = False
		#restart the game
		if (not self.stats.game_active) and (event.key == pygame.K_SPACE):
			self.player = pygame.sprite.GroupSingle(Player(self))
			self.start_time = pygame.time.get_ticks()
			self.session_score = 0
			self.rocks.empty()
			self.rock_count = 0
			self.stats.game_active = True

	def _update_screen(self):
		"""Update images on the screen, and flip to the new screen."""
		self.screen.fill(self.settings.background_color)
		self.player.sprite.blitme()
		self.rocks.draw(self.screen)
		self._update_score()
		#if game is ended, display appropriate string
		if not self.stats.game_active:
			self._game_over()

		pygame.display.flip()

	def _create_rock(self):
		"""Create a fleet of rocks."""
		rock = Rock(self)

		self.rocks.add(rock)
		self.rock_count +=1

	def _update_rocks(self):
		"""Updates all rock images on the screen."""
		#Update each rock's position
		self.rocks.update()

		#Get rid of rocks that have disappeared
		for rock in self.rocks.copy():
			if rock.at_edge():
				self.rocks.remove(rock)
				self.rock_count -= 1

		self._check_rock_player_collisions()

	def _check_rock_player_collisions(self):
		"""Respond to rock-player collisions. Ends the game."""
		for rock in self.rocks:
			if self.player.sprite.rect.colliderect(rock):
				self.stats.game_active = False
				self.rocks.empty()

	def _update_score(self):
		"""Updates the score based on the amount of time alive"""
		#Stops updating when gamestate is inactive
		if self.stats.game_active:
			self.timer_text = str((pygame.time.get_ticks() - self.start_time)/1000).zfill(3)
			self.timer_text = self.font.render("Score: " + self.timer_text, 1, (0, 0, 0))

		self.screen.blit(self.timer_text, self.timer_rect)

	def _game_over(self):
		"""When game is over, display 'Game Over!' text """
		if self.stats.game_active is True:
			self.session_score = float((pygame.time.get_ticks() - self.start_time)/1000)
			#self._check_score()
			self.stats.game_active = False

		self.screen.blit(self.game_over_text, self.game_over_rect)

	def _check_score(self):
		#TODO
		"""Called once when the game ends to see if you have new high score"""
		file = open('scoring.txt', 'r+')
		high_score = file.read()
		#if your score > high score, update high score
		if self.session_score > float(high_score):
			file.truncate(0)
			print(f"{self.session_score}")
			print(f"{str(self.session_score)}")
			print(f"{high_score}")
			print(f"{float(high_score)}")

			file.write(f"{self.session_score}")
		file.close()


if __name__ == '__main__':
	#Make a game instance, then run it
	ai = MyGame()
	ai.run_game()
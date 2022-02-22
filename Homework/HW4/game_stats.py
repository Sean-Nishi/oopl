"""
Sean Nishi
10/30/2021
Homework 4
"""

class GameStats:
	"""Track statistics for rock game"""

	def __init__(self, rock_game):
		"""Initialize statistics"""
		self.settings = rock_game.settings
		self.reset_stats()

		#Start rock game in an active state.
		self.game_active = True

	def reset_stats(self):
		"""Initialize statistics that can change during the game"""
		self.lives = self.settings.starting_lives
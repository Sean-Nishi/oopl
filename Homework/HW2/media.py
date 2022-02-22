#Sean Nishi
#Homework #2 Python OO
#Part 2 media.py

class SocialMedia:
	def __init__(self, platformName, platformURL):
		"""Receives the name of the social media and the URL"""
		self.platformName = platformName
		self.platformURL = platformURL

	def postMessage(self, msg):
		"""Receives a message msg and then posts it to the platform via the URL"""
		print(f"Posting not implemented in base class")


class Twitter(SocialMedia):
	def __init__(self, platformName, platformURL):
		"""Inits the base class with the platform values"""
		super().__init__(platformName, platformURL)

	def postMessage(self, msg):
		"""Receives a message msg and then posts it to the platform via the URL"""
		if len(msg) <= 80:
			print(f"Posting message to Twitter: {msg}")
		else:
			print(f"Message is too long.")


class Facebook(SocialMedia):
	def __init__(self, platformName, platformURL):
		"""Inits the base class with the platform values"""
		super().__init__(platformName, platformURL)

	def postMessage(self, msg):
		"""Receives a message msg and then posts it to the platform via the URL"""
		print(f"Posting message to all your friends on Facebook: {msg}")


class LinkedIn(SocialMedia):
	def __init__(self, platformName, platformURL):
		"""Inits the base class with the platform values"""
		super().__init__(platformName, platformURL)

	def postMessage(self, msg):
		"""Receives a message msg and then posts it to the platform via the URL"""
		print(f"Posting message to all your colleagues on LinkedIn: {msg}")

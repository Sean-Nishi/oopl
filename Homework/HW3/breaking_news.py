"""
Sean Nishi
10/15/2021
Homework 3 Part 2
Breaking News App
"""

from abc import ABC, abstractmethod

class Publisher(ABC):
	"""Base class that publishes updates to all subscribers to pick up"""

	@abstractmethod
	def attach(self, subscriber):
		"""Attach a subscriber to the publisher"""
		pass

	@abstractmethod
	def detach(self, subscriber):
		"""Detach a subscriber from the publisher"""
		pass

	@abstractmethod
	def notify(self):
		"""Notify all subscribers about an event"""
		pass

class NewYorkTimesBreakingNews(Publisher):
	"""Derived from Publisher, will update subscribers with NYTimes news"""

	def __init__(self):
		"""Constructor. Creates the subscribers"""
		self._subscribers = []

	def attach(self, subscriber):
		"""Attach a subscriber to the publisher"""
		self._subscribers.append(subscriber)

	def detach(self, subscriber):
		"""Detach a subscriber from the list"""
		self._subscribers.remove(subscriber)

	def publish_news_item(self, news_category, news_title):
		"""Publishes a new news item"""
		print(f"NYT: Breaking News: {news_title}. [category = {news_category}]")
		self.notify(news_category, news_title)

	def notify(self, news_category, news_title):
		"""Notify all subscribers"""
		print(f"NYT: Notifying subscribers...")
		for subscriber in self._subscribers:
			subscriber.breaking_news(news_category, news_title)


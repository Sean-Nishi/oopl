"""
Sean Nishi
10/15/2021
Homework 3 Part 2
Breaking News App
"""

from abc import ABC, abstractmethod

class Subscriber:
	"""Base subscriber class"""

	@abstractmethod
	def breaking_news(self, news_category, news_title):
		"""Notifies the subscriber of new news"""
		pass

class BusinessNewsSubscriber(Subscriber):
	"""Subscriber that only cares about business news"""

	def breaking_news(self, news_category, news_title):
		"""Implementation for business news. Will notify subscriber of business news"""
		if news_category == "business":
			print(f"Subscriber: Business Breaking: {news_title}")

class PoliticsNewsSubscriber(Subscriber):
	"""Subscriber that only cares about political news"""

	def breaking_news(self, news_category, news_title):
		"""Implementation for business news. Will notify subscriber of business news"""
		if news_category == "politics":
			print(f"Subscriber: Politics Breaking: {news_title}")

class KeyWordSubscriber(Subscriber):
	"""Subscriber that filters news by keyword"""

	def __init__(self, keyword):
		"""Subscriber that only cares about keyword news"""
		self._keyword = keyword

	def breaking_news(self, news_category, news_title):
		"""Implementation for business news. Will notify subscriber of business news"""
		if self._keyword.lower() in news_title.lower():
			print(f"Subscriber: Filter [{self._keyword}]: {news_title}")
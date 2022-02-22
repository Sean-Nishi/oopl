"""
Sean Nishi
10/15/2021
Homework 3
run.py
"""

"""
Run the Breaking News Observer Pattern.
"""
from breaking_news import NewYorkTimesBreakingNews
from subscriber import BusinessNewsSubscriber
from subscriber import PoliticsNewsSubscriber
from subscriber import KeyWordSubscriber

# The client code.
nyt = NewYorkTimesBreakingNews()

subscriber_a = BusinessNewsSubscriber()
nyt.attach(subscriber_a)

subscriber_b = PoliticsNewsSubscriber()
nyt.attach(subscriber_b)

subscriber_c = KeyWordSubscriber("biden")
nyt.attach(subscriber_c)

nyt.publish_news_item("business", "Facebook goes down for 5 hours.")
nyt.publish_news_item("politics", "Biden calls for debt limit ceiling to be raised.")

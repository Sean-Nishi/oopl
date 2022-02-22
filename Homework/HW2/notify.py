#Sean Nishi
#10/1/2021
#Homework 2 Part 2 notify.py

import media

newTwitter = media.Twitter("Twitter", "https://twitter.com/")
newFacebook = media.Facebook("Facebook", "https://facebook.com/")
newLinkedIn = media.LinkedIn("LinkedIn", "https://LinkedIn.com/")


newTwitter.postMessage("This is a significatly longer message. It is meant to trigger the Twitter class's 'Message is too long' message. Let's see if it worked...")
newTwitter.postMessage("Short Message")

newFacebook.postMessage("Hello my friends!!!")

newLinkedIn.postMessage("Hello my colleagues!!!")
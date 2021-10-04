import tweepy

#Import authentication keys
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

# Creates object that has permission to use your personal twitter account
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# Gives account permission to use Twitter API
auth.set_access_token(access_token, access_token_secret)

#Create object twitter of Twython and pass in keys
twitter = tweepy.API(auth)

message = "Hello IEEE!"

#Calls update_status method in Tweepy and passes in your message

twitter.update_status(status=message)

#twitter.update_with_media('1200px-IEEE_logo.png', message)

print("Tweeted: %s" % message)
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

#Change message value to change tweet
message = "Hello IEEE!!!!"

#Calls update_status method in Tweepy and passes in your message
twitter.update_status(status=message)

#Uncomment this update status and comment other one to tweet out message with picture
#twitter.update_status_with_media(status = message, filename ='1200px-IEEE_logo.png')

print("Tweeted: %s" % message)
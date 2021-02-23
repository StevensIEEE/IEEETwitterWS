import tweepy


#Import authentication keys
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)   
auth.set_access_token(access_token, access_token_secret)

#Create object twitter of Twython and pass in keys
twitter = tweepy.API(auth)

message = "Hello IEEE!"

#Calls update_status method in Tweepy and passes in your message

twitter.update_status(status=message)
print("Tweeted: %s" % message)

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

#timeline = twitter.home_timeline()
#print(timeline)

tweets = twitter.user_timeline('@bodega_cats')
print(tweets)

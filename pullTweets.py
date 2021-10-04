import tweepy
import wget

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

#uncomment for to get json description of home timeline. Mostly useless for us
#timeline = twitter.home_timeline()
#print(timeline)


tweets = twitter.user_timeline(screen_name='@memeadikt')

#prints tweets for user specified
print(tweets)

media_files = set()
for status in tweets:
    media = status.entities.get('media', [])
    if(len(media) > 0):
        media_files.add(media[0]['media_url'])

for media_file in media_files:
    wget.download(media_file)



#print(tweets[0].text)
#for tweet in tweets:
#    print(tweet.text)

#followers = twitter.followers()[0].name
#print("My followers: {}".format(followers))
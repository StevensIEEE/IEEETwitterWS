#Import the necessary methods from tweepy library
import tweepy
import os

#Import authentication keys
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)
counter = 0
filename = "results.txt"
class StreamListener(tweepy.Stream):

    def on_data(self, raw_data):

        global counter
        global filename
        if(counter < 30):
            print(raw_data)
            counter +=1
            with open(filename, 'a') as file:
                file.write(raw_data.decode('utf-8'))
        else:
            quit()

if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    stream = StreamListener(consumer_key,consumer_secret,access_token,access_token_secret)
    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['Jets', 'Giants', 'Football'])

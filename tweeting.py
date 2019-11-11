from twython import Twython

#Import authentication keys
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

#Create object twitter of Twython and pass in keys
twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

message = "Hello IEEE!"

#Calls update_status method in Twython and passes in your message

twitter.update_status(status=message)
print("Tweeted: %s" % message)

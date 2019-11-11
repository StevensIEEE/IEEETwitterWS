from twython import Twython
import glob


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


#Loads images from picture folder
images = glob.glob("1200px-IEEE_logo.png")
#images = glob.glob("/home/iengel/projects/twitterAPI/tweetingDemo/1200px-IEEE_logo.png")

#Opens most recent picture and tweets it
if len(images) > 0:
    image_open = open(images[len(images)-1], "rb")
    image_ids = twitter.upload_media(media=image_open)
    print: "Image ID received"
    twitter.update_status(status = 'I can tweet pictures too!',media_ids =[image_ids['media_id']])

#Commented out this test code to get one pic tweeting working
#pic = open("/home/iengel/projects/twitterAPI/tweetingDemo/1200px-IEEE_logo.svg.png" ,"rb")
#image_id = twitter.upload_media(media=pic)
#twitter.update_status(status = "Hopefully this one actually works!", media_ids=[image_id['media_id']])

#print("Tweeted Picture")

else:
    print: "no pictures in that folder"

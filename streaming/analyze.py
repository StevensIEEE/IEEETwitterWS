import json
import pandas as pd
import matplotlib.pyplot as plt

# Location of the file where you saved the tweets
tweets_data_path = 'results.txt'

# Read the tweets out of the file and append them to a list
tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue


print('There were ', len(tweets_data), ' tweets recorded')

# Put the tweets into the proper format for pandas
tweets = pd.DataFrame()

# Get data on the contents of the tweets, language they're in, and where they came from
tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)
tweets['lang'] = map(lambda tweet: tweet['lang'], tweets_data)
tweets['country'] = map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_data)


tweets_by_lang = tweets['lang'].value_counts()

# Plot the data for languages
fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Languages', fontsize=15)
ax.set_ylabel('Number of tweets' , fontsize=15)
ax.set_title('Top 5 languages', fontsize=15, fontweight='bold')
tweets_by_lang[:5].plot(ax=ax, kind='bar', color='red')

plt.show()


tweets_by_country = tweets['country'].value_counts()

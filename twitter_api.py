from keys import *
import os
import os.path
from os import path
import tweepy

def get_feed(twitter_handle,numTweets):
    
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    # Print Twitter Feed of a User
    public_tweets = api.user_timeline(screen_name=twitter_handle, count=numTweets)

    # Init list to collect tweets
    queue = []
    for tweet in public_tweets:
        if len(tweet.text) > 40:
            queue.append(tweet.text[0:40] + '...')
        else:
            queue.append(tweet.text)

    return queue

def check_keys():
    if path.exists('keys.py'):
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
    else:
        print('File \'keys.py\' does not exist. Please enter your keys in a \'keys.py\' file in this directory')
        return
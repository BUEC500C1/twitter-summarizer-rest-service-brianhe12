#from keys import *
import os
import os.path
from os import path
import tweepy
import concurrent.futures

def get_feed(twitter_handle,numTweets):
    auth = tweepy.OAuthHandler(os.environ['CONSUMER_KEY'], os.environ['CONSUMER_SECRET'])
    auth.set_access_token(os.environ['ACCESS_TOKEN'],os.environ['ACCESS_TOKEN_SECRET'])
    api = tweepy.API(auth)

    # Print Twitter Feed of a User
    public_tweets = api.user_timeline(screen_name=twitter_handle, count=numTweets)

    # Init list to collect tweets
    queue = []
    def get_tweets_from_public_tweets(public_tweets):
        if len(public_tweets.text) > 40:
            queue.append(public_tweets.text[0:40] + '...')
        else:
            queue.append(public_tweets.text)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(get_tweets_from_public_tweets, public_tweets)

    return queue

def check_keys():
    if path.exists('keys.py'):
        pass
    else:
        print('File \'keys.py\' does not exist. Please enter your keys in a \'keys.py\' file in this directory')
        quit()


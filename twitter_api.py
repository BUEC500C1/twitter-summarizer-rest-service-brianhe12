from keys import *

def get_feed(twitter_handle,numTweets):
    import tweepy
    import os
    

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)

    # Print Twitter Feed of a User
    public_tweets = api.user_timeline(screen_name=twitter_handle, count=numTweets)

    # Init list to collect tweets
    s1 = []
    for tweet in public_tweets:
        if len(tweet.text) > 40:
            s1.append(tweet.text[0:40] + '...')
        else:
            s1.append(tweet.text)

    return s1
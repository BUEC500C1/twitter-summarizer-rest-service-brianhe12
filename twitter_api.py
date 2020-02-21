def get_feed(twitter_handle,numTweets):
    import tweepy
    from dotenv import load_dotenv
    import os

    load_dotenv()

    auth = tweepy.OAuthHandler(os.getenv("CONSUMER_KEY"), os.getenv("CONSUMER_SECRET"))
    auth.set_access_token(os.getenv("ACCESS_TOKEN"), os.getenv("ACCESS_TOKEN_SECRET"))

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
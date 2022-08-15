from re import search
import time 
import tweepy 
import random



api_key = ""
api_secret = ""
bearer_token = r""
access_token = ""
access_token_secret = ""

# Gainaing access and connecting to Twitter API using Credentials
client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)

# Creating API instance. This is so we still have access to Twitter API V1 features
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

#search tweet with NFT keyword and if it has more than 1000 like retweet it
def search_tweet(keyword):
    count = 0
    for tweet in tweepy.Cursor(api.search_tweets, q = keyword,
                                tweet_mode = 'extended').items(1000):
        if tweet.retweet_count < 10:
            try:
                api.create_favorite(tweet.id)
                print(f"{count}- Liked a tweet")
                time.sleep(random.randint(180,220))  #set your own random time sleep, it should be somewhere between 1.5 and 3 minutes
                count+=1
            except:
                continue
        else:
            continue
#write your keyword you want to like
search_tweet("")
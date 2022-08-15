from unicodedata import name
import tweepy
import time
import random 
# import pandas

# Credentials
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

def search_users(keyword):
    names = []
    usernames = []
    user_id =[]
    user_description = []
    user_followers = []
    user_following = []
    for user in tweepy.Cursor(api.search_users, q = keyword,
                               tweet_mode = 'extended').items(1000):
            usernames.append(user.screen_name)
            names.append(user.name)
            user_id.append(user.id)
            user_description.append(user.description)
            user_followers.append(user.followers_count)
            user_following.append(user.friends_count)
    return names,usernames,user_id,user_description,user_followers,user_following
users = search_users("NFT project")
with open('''NFT Collection.txt''',"r") as t:
    f = [i for i in t.read().splitlines()]
    for i in range(375,len(users[1])-1):
        if users[1][i] not in f:
            try:
                time.sleep(random.randint(90,110))
                mytext = "Write your messages Here'"
                api.send_direct_message(recipient_id=users[2][i],text= mytext)
                print(f"{i}- sent a DM to {users[1][i]}")

            
        








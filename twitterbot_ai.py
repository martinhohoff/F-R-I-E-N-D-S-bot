import tweepy
from time import sleep
from credentials import *
from sample import *
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
thistext = main()
api.update_status(thistext)
print (thistext)
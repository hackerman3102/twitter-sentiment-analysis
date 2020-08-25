from tweepy import Stream
import keys
import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
import json
from textblob import TextBlob
consumer_key=keys.ck
access_token=keys.at
access_token_secret=keys.ats
consumer_secret_key=keys.csk
auth = tweepy.OAuthHandler(consumer_key,consumer_secret_key)
auth.set_access_token(access_token, access_token_secret)
api=tweepy.API(auth)
pos=0
neg=0
ne=0
public_tweets=api.search('#India')#Your Keyword goes here
for tweet in public_tweets:
    print(tweet.text)
    analysis=TextBlob(tweet.text)
    a=analysis.sentiment.polarity
    print(analysis.sentiment)
    if(a>0):
        pos+=1
    if(a<0):
        neg+=1
    else:
        ne+=1
pos=100*pos/len(public_tweets)
neg=100*neg/len(public_tweets)        
print(len(public_tweets))
print("positive tweets = {} %" .format(pos))
print("Negative Tweets ={} %".format(neg))
        
    


            
        
        

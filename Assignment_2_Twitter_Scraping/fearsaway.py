import datetime
import pandas as pd
import tweepy
from datetime import date
import configparser
import datetime, time

#Script to scrap data from twitter and writing in a csv file

#Reading configurations using configparser
config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']
acess_token = config['twitter']['access_token']
acess_token_secret = config['twitter']['access_token_secret']

#Authentication 
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(acess_token, acess_token_secret)

api = tweepy.API(auth)


now = datetime.date.today()
date_since = datetime.datetime.strptime(time.strftime("%Y-%m-%d"), "%Y-%m-%d")
print (date_since)
num_tweets=50
print ("num_tweets ", num_tweets)

new_search = "#crime -filter:retweets"

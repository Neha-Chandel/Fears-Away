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

# Using .Cursor() to search through twitter for the tweets with passed keyword
# Limiting the number of tweets by using .items(number of tweets)
tweets = tweepy.Cursor(api.search_tweets,
              q=new_search,
              lang="en",
              tweet_mode='extended').items(num_tweets)

cnt=0

#Creating dataframe

tcolumns = ['twitter_id','twitter_handle','twitter_text', 'created_at' ,'hashtag','retweets']
tdata = []
ucolumns = [ 'twitter_handle', 'user_name', 'user_location', 'user_type', 'total_tweets', 'follower_count', 'following_count', 'created_at']
udata=[]

#Appending data

for tweet in tweets:
    tdata.append([tweet.id,tweet.user.name,  tweet.user.description, tweet.created_at, tweet.entities['hashtags'], tweet.retweet_count]) 
    udata.append([tweet.user.name, tweet.user.screen_name, tweet.user.location, tweet.user.verified, tweet.user.statuses_count, tweet.user.followers_count, tweet.user.friends_count, tweet.user.created_at])
    cnt=cnt+1

#Using the dataframes
#I have created 2 dataframes as I am using the data from 2 tables and inserting the data from
#2 different cvs files

df1 = pd.DataFrame(udata, columns=ucolumns)
df2 = pd.DataFrame(tdata,columns=tcolumns)

print(df1)
print(df2)

#Converting the dataframes to cvs file
df1.to_csv('tweets1.csv', index=False)
df2.to_csv('tweets2.csv', index=False)

	



	

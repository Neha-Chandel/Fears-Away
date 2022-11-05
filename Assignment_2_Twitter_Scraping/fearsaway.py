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


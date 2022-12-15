import mysql.connector
import csv
import pandas as pd

conn=mysql.connector.connect(host='localhost', username='root', password='admin', database='fear_away')
my_cursor=conn.cursor()
csv_data1 = (csv.reader(open('tweets1.csv', encoding="utf8")))

# store headers and rows

header = next(csv_data1)

print ("importing the file 1")

for row in csv_data1:
    print(row)
    my_cursor.execute("INSERT INTO user (twitter_handle, user_name, location, user_type, total_tweets, follower_count, following_count, join_date) VALUES(%s, %s, %s, %s, %s, %s, %s,%s)", row)

print ("Loaded in User Database")

csv_data2 = (csv.reader(open('tweets2.csv',encoding="utf8")))
header = next(csv_data2)
print ("importing the file 2")
for row in csv_data2:
    print(row)
    my_cursor.execute("INSERT INTO tweets (tweet_id ,twitter_handle, tweet_description, created_at, hashtags, retweet_count) VALUES(%s, %s, %s, %s, %s,%s)", row)
conn.commit()
print ("Loaded in Tweets Database")
conn.close()

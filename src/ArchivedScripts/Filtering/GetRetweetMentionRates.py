'''
INPUT Parameters: 
    - A directory name that contains immigrant objects
    - A directory name that contains the tweet files
'''

import tweepy 
import pickle
import os
import sys
from datetime import datetime
import time
import operator




class Immigrant(object):
    def __init__(self,user_id, immigration_date,tweets,source_country,destination_country, duration):
        self.user_id = user_id
        self.immigration_date = immigration_date
        self.tweets = tweets
        self.source_country = source_country
        self.destination_country = destination_country
        self.duration = duration
        
    def display(self):
        print('**********************************')
        print('user id:', self.user_id)
        print('# of tweets', len(self.tweets))
        print('immigrated from: ', self.source_country)
        print('to: ', self.destination_country)
        print('at:', self.immigration_date)
        print('for', self.duration, 'days')
        print('**********************************')



start_time = datetime.now()
print('started at:', datetime.now().time())


immigrants = os.listdir(sys.argv[1])

print(str(len(immigrants)) + ' immigrants found so far')

src = {}
dest = {}
src_dest = {}


stats_file = open("immigrant_stats.csv", "w")

for immigrant in immigrants: 
    f = open(sys.argv[1] + immigrant, 'rb')
    immigrant_obj = pickle.load(f)
    f.close()

    f = open(sys.argv[2] + immigrant, 'rb')
    tweets = pickle.load(f)
    f.close()

    after_no = 0
    after_retweet = 0
    after_reply = 0

    before_no = 0
    before_retweet = 0
    before_reply = 0

    first_tweet_date = tweets[0].created_at

    for tweet in tweets: 
        if tweet.created_at > immigrant_obj.immigration_date: 

            #tweet is made after the immigration:
            after_no += 1
            if(tweet.retweeted):
                after_retweet += 1
            if(tweet.in_reply_to_user_id != None):
                after_reply += 1

        else: 

            #tweet is made before the immigration:
            before_no = before_no + 1
            if(tweet.retweeted):
                before_retweet += 1
            if(tweet.in_reply_to_user_id != None):
                before_reply += 1

        #Get Date of first tweet
        if(tweet.created_at < first_tweet_date):
            first_tweet_date = tweet.created_at


    stats_file.write(immigrant + ',')
    stats_file.write(str((immigrant_obj.immigration_date - first_tweet_date).days) + ',')
    stats_file.write(str(immigrant_obj.immigration_date) + ',')
    stats_file.write(str(len(tweets)) + ',')
    stats_file.write(immigrant_obj.source_country + ',')
    stats_file.write(immigrant_obj.destination_country + ',')
    stats_file.write(str(immigrant_obj.duration) + ',')
    stats_file.write(str(after_no) + ',')
    stats_file.write(str(after_retweet) + ',')
    stats_file.write(str(after_reply) + ',')
    stats_file.write(str(before_no) + ',')
    stats_file.write(str(before_retweet) + ',')
    stats_file.write(str(before_reply) + '\n')

stats_file.close
    

    




print('\n***************************')
end_time = datetime.now()
print('done at:', end_time.time())
print('script took:', end_time - start_time)


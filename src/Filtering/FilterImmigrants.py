'''
GET all tweet information for all IDs in a a given file
Also prunes those IDs that are not interesting for us
INPUT Parameters: 
    - A directory name that contains all tweets. a user per file
    - A directory to store Immigrants. an immigrant object per file
'''

import tweepy 
import pickle
import os
import sys
from datetime import datetime
import time

#parameters:
min_status_count = 100

ACCESS_TOKEN = '3007366663-QU3WM6hrAXEAfelPzdCpv713LOB8D7LgtsuvZWL'
ACCESS_SECRET = 'RzDTCkg3xoZfEmc3bGNXypponiq06ak9rZxiziXzx7nkO'
CONSUMER_KEY = 'nlbCSYMdqtyKpANbLQOl6ITKZ'
CONSUMER_SECRET = 'wY1CXDFLcN03H94BQo96KzKW47J2nfvoQBr4x5XL96POTV9Bbj'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)
api.wait_on_rate_limit = True
api.wait_on_rate_limit_notify = True


class User_Tweet(object):
    def __init__(self,date,text,country):
        self.date = date
        self.text = text
        self.country = country

def build_timeline(tweets):
    timeline = []
    for tweet in tweets: 
        if tweet.place is not None: 
            user_tweet = User_Tweet(tweet.created_at, tweet.text, tweet.place.country)
            timeline.append(user_tweet)
    return sorted(timeline, key=lambda x: x.date)

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

def is_immigrant(user_id, timeline):
    
    countries = []
    for user_tweet in timeline:
        if user_tweet.country not in countries:
            countries.append(user_tweet.country)

    if (len(countries) > 1):
        if timeline[-1].country == countries[-1]:
            #find the time of last tweet in the previous country
            i = len(timeline) - 1
            last_tweet_previous_country = timeline[i]
            while(last_tweet_previous_country.country != countries[-2]):
                i = i - 1
                last_tweet_previous_country = timeline[i]
            
            duration = timeline[-1].date - last_tweet_previous_country.date
            if duration.days > 90:
                #lets reload ALL his/her tweet:
                file_name = sys.argv[1] + str(user_id)
                f = open(file_name,'rb')
                tweets = pickle.load(f)
                f.close()
                
                #now lets build him/her in form of an Immigrant object:
                immigrant = Immigrant(user_id, last_tweet_previous_country.date, tweets,last_tweet_previous_country.country,timeline[-1].country,duration.days)

                return True, immigrant
    return False, None


def process(tid, tweets_directory): 
    f = open(tweets_directory + tid, 'rb')
    tweets = pickle.load(f)
    f.close()

    timeline = build_timeline(tweets)
    is_imm, immigrant = is_immigrant(tid, timeline)

    if is_imm  == True: 
        return True, immigrant
    else: 
        return False, None


start_time = datetime.now()
print('started at:', datetime.now().time())

while(True):
    #Get all ids
    all_IDs = os.listdir(sys.argv[1])

    #Get processed(filtered) IDs
    f = open('filtered', 'r')
    filtereds = []
    for line in f:
        filtereds.append(line.split('\n')[0])
    f.close()

    #exclude already processed ones
    twitter_ids = [x for x in all_IDs if x not in filtereds]

    print(str(len(twitter_ids)) + ' new accounts to process')
    #if nothing to process, wait for 10 minutes
    if(len(twitter_ids) == 0):
        print('No new tweeter account to process is available.')
        print('Everything is prcessed. Waiting for 10 minutes.')
        time.sleep(10*60)
        continue

    #process
    for tid in twitter_ids: 
        try:
            is_imm, immigrant = process(tid, sys.argv[1])
            if is_imm:
                f = open(sys.argv[2] + '/' + tid, 'wb')
                pickle.dump(immigrant, f)
                immigrant.display()
                f.close()
            f = open('filtered', 'a')
            f.write(tid + '\n')
            f.close()
        except:
            print('An error captured')
            pass


print('\n***************************')
end_time = datetime.now()
print('done at:', end_time.time())
print('script took:', end_time - start_time)


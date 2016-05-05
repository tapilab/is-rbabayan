'''
INPUT Parameters: 
    1. Training file name
    2. Immigrants folder
    3. All Tweets folder
'''

import tweepy 
import pickle
import os
import sys
from datetime import datetime
import time
import json
from pprint import pprint 
import nltk
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import copy
from collections import Counter
import urllib.request

class UserFeature(object):
    def __init__(self, user_id, location, followers_count, gender, tweets_dates, replies_dates):
        self.user_id = user_id
        self.location = location
        self.followers_count = followers_count
        self.gender = gender
        self.tweets_dates = tweets_dates
        self.replies_dates = replies_dates

    def display(self):
        print('**********************************')
        print('user id:', self.user_id)
        print('location', self.location)
        print('followers count: ', str(self.followers_count))
        print('gender: ', str(self.gender))
        print('Number of tweets:', str(len(self.tweets_dates)))
        print('Number of replies:', str(len(self.replies_dates)))
        print('**********************************')



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


def load_census():
    female_url = "http://www2.census.gov/topics/genealogy/1990surnames/dist.female.first"
    male_url = "http://www2.census.gov/topics/genealogy/1990surnames/dist.male.first"
                
    female_request = urllib.request.urlopen(female_url)
    male_request = urllib.request.urlopen(male_url)

    line2name = lambda x: x.decode('utf-8').split()[0].lower() if x else ''
    
    females = []
    males = []
    
    for line in female_request:
        females.append(line2name(line).lower())

    for line in male_request:
        males.append(line2name(line).lower())

    set_male = set(males)
    set_female = set(females)

    set_ambiguous = set_female & set_male
    set_female -= set_ambiguous
    set_male -= set_ambiguous

    return set_male, set_female


def get_gender_api(name):
    print('API had to be called')
    try:
        json_result = urllib.request.urlopen("https://api.genderize.io/?apikey=9ba7964e74c51c9663200446d7ed1f3c&name="+name).read()
        gender = json.loads(json_result.decode('utf-8'))['gender']
        return gender
    except Exception as e:
        print("Exception in reading from Genderize API:")
        print(str(e))
        return None

def get_gender(male_names, female_names, name):
    name = name.lower()
    if name in male_names:
        return 'male'
    elif name in female_names:
        return 'female'
    
    gender = get_gender_api(name)
    if gender is not None:
        return gender
    else:
        return 'unknown'

start_time = datetime.now()
print('started at:', datetime.now().time())

male_names, female_names = load_census()

immigrants = os.listdir(sys.argv[1])
all_users = os.listdir(sys.argv[2])
non_immigrants = [i for i in all_users if i not in immigrants]

candidates = []
i = 0
for user in non_immigrants:
    try:
        f = open(sys.argv[2] + user, 'rb')
        tweets = pickle.load(f)
        f.close()


        if tweets[0].user.lang != 'en':
            continue

        name = tweets[0].user.name.split(' ')[0].lower()
        gender = get_gender(male_names, female_names, name)

        replies_dates = []
        dates = []
        locations = []
        for tweet in tweets:
            if tweet.in_reply_to_user_id != None: 
                replies_dates.append(tweet.created_at)
            dates.append(tweet.created_at)
            if tweet.place is not None:
                locations.append(tweet.place.country)
        if(len(locations) > 0):
            location, no = Counter(locations).most_common(1)[0]
    
            features = UserFeature(user, location, tweets[0].user.followers_count, gender, dates, replies_dates)
            candidates.append(features)


        #print("No location info available for this user")

        if len(candidates) == 1000:
            f = open("Candidates2/candidates_" + str(i), "wb")
            pickle.dump(candidates, f)
            f.close()
            candidates = []
            print("************* An output file saved")

        i += 1
        print(str(len(candidates)) + ' from ' + str(i))
    except Exception as e:
        print("Exception Handled!")
        print(str(e))
        pass

if len(candidates) > 0:
    f = open("Candidates2/candidates_" + str(i), "wb")
    pickle.dump(candidates, f)
    f.close()

'''
candidates_filenames = os.listdir("Candidates/")
print(str(len(candidates_filenames)))
for can_file in candidates_filenames:
    f = open("Candidates/" + can_file, "rb")
    candidates = pickle.load(f)
    f.close()
    print(len(candidates))
    candidates[0].display()



for immigrant in immigrants[:1]:

    f = open(sys.argv[1] + immigrant, 'rb')
    immigrant_obj = pickle.load(f)
    f.close()
    
    f = open(sys.argv[2] + immigrant, 'rb')
    tweets = pickle.load(f)
    f.close()

    location = immigrant_obj.source_country
    number_followers = tweets[0].user.followers_count

    number_tweets_before = 0
    for tweet in tweets:
        if tweet.created_at <= immigrant_obj.immigration_date:
            number_tweets_before += 1
    
    date_first_tweet = tweets[-1].created_at

'''
print('\n***************************')
end_time = datetime.now()
print('done at:', end_time.time())
print('script took:', end_time - start_time)

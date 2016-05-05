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
from scipy.spatial import distance


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

def get_no_tweets_per_day(imm_date, tweet_dates):
    tweet_dates_before = []
    for tweet_date in tweet_dates:
        if tweet_date < imm_date:
            tweet_dates_before.append(tweet_date)
    no = len(tweet_dates_before)
    if len(tweet_dates_before) == 0:
        return 0
    days = abs((tweet_dates_before[0] - tweet_dates_before[-1]).days)
    if days != 0:
        return (no * 1.0) / days
    return 0

def get_no_replies_per_day(imm_date, tweet_dates, replies_dates):
    replies_dates_before = []
    for reply_date in replies_dates:
        if reply_date < imm_date:
            replies_dates_before.append(reply_date)
    no = len(replies_dates_before)
    days = abs((imm_date - tweet_dates[-1]).days)
    if days != 0:
        return (no * 1.0) / days
    return 0

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
        json_result = urllib.request.urlopen("https://api.genderize.io/?name="+name).read()
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


users_feature_files = os.listdir('Candidates2')
candidates_features = []
for user_feature_file in users_feature_files:
    f = open('Candidates2/' + user_feature_file, 'rb')
    candidates_features.extend(pickle.load(f))
    f.close()

    print('loading candidates features: ' + str(len(candidates_features)) + ' candidates loaded.')

imm_feature_files = os.listdir('ImmigrantsFeatures/')

locations = []
for imm_feature_file in imm_feature_files:
    f = open('ImmigrantsFeatures/' + imm_feature_file, 'rb')
    imm_features = pickle.load(f)
    f.close()

    locations.append(imm_features.location)

locations_set = set(locations)

selected_can_features = []
for can_features in candidates_features:
    if can_features.location in locations_set:
        selected_can_features.append(can_features)


similars = []

result_file = open('CandidatesPerImmigrant/similars.csv', 'w')
for imm_feature_file in imm_feature_files:
    f = open('ImmigrantsFeatures/' + imm_feature_file, 'rb')
    imm_features = pickle.load(f)
    f.close()

    f = open('../Filtering/Immigrants/' + imm_feature_file, 'rb')
    imm_object = pickle.load(f)
    f.close()

    imm_tweets_per_day = get_no_tweets_per_day(imm_object.immigration_date, imm_features.tweets_dates)
    imm_reply_per_day = get_no_replies_per_day(imm_object.immigration_date, imm_features.tweets_dates, imm_features.replies_dates)
    imm_followers = imm_features.followers_count
    imm_days =abs((imm_features.tweets_dates[-1] - datetime(2006,7,15,0,0,0)).days)

    imm_vec = np.array([imm_tweets_per_day, imm_reply_per_day, imm_followers, imm_days])

    can_per_imms = []
    distances = []
    for can_features in selected_can_features:
        if can_features.location == imm_features.location and can_features.gender == imm_features.gender:
            
            can_tweets_per_day = get_no_tweets_per_day(imm_object.immigration_date, can_features.tweets_dates)
            can_followers = can_features.followers_count
            can_reply_per_day =  get_no_replies_per_day(imm_object.immigration_date, can_features.tweets_dates, can_features.replies_dates)
            can_days = abs((can_features.tweets_dates[-1] - datetime(2006,7,15,0,0,0)).days)

            can_vec = np.array([can_tweets_per_day, can_reply_per_day, can_followers, can_days])

            d =  distance.cosine(can_vec, imm_vec)
            distances.append((d, can_features, can_vec))
    
    distances = sorted(distances, key = lambda x:x[0])

    found_flag = False
    if len(distances) > 0:
        for i in distances:
            sim_id = i[1].user_id 
            if sim_id not in similars:
                similars.append(sim_id)
                found_flag = True
                result_file.write(str(imm_features.user_id) + ',' + str(sim_id) + '\n')
                print('Found a similar user: ' + str(sim_id))
                break

    if found_flag == False:
        result_file.write(str(imm_features.user_id) + ',\n')

    print('so far found ' + str(len(similars)) + ' similar user accounts')
    
result_file.close()

'''
male_names, female_names = load_census()

immigrants = os.listdir(sys.argv[1])
all_users = os.listdir(sys.argv[2])

already_dones = os.listdir('ImmigrantsFeatures/')

i = 0
for user in immigrants:
    try:
        f = open(sys.argv[2] + user, 'rb')
        tweets = pickle.load(f)
        f.close()

        if user in already_dones:
            print('Already processed: ' + user)
            continue

        #ignore non english users:
        if tweets[0].user.lang != 'en':
            continue 

        name = tweets[0].user.name.split(' ')[0].lower()
        gender = get_gender(male_names, female_names, name)

        dates = []
        locations = []
        for tweet in tweets:
            dates.append(tweet.created_at)
            if tweet.place is not None:
                locations.append(tweet.place.country)
        if(len(locations) > 0):
            location, no = Counter(locations).most_common(1)[0]
    
            features = UserFeature(user, location, tweets[0].user.followers_count, gender, dates)

            file_output = open('ImmigrantsFeatures/' + user, 'wb')
            pickle.dump(features, file_output)
            file_output.close()

        i += 1
        print(str(i))

    except Exception as e:
        print("Exception Handled:")
        print(str(e))
        pass

'''
print('\n***************************')
end_time = datetime.now()
print('done at:', end_time.time())
print('script took:', end_time - start_time)

'''
GET all tweet information for all IDs in a a given file
Also prunes those IDs that are not interesting for us
INPUT Parameters: 
    - File name that contains all IDs to get tweets of
    - A directory name to store all tweets. a user per file
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

start_time = datetime.now()
print('started at:', datetime.now().time())

#Get IDs
f = open(sys.argv[1], 'rb')
all_IDs = pickle.load(f)
print('Found ', len(all_IDs), 'twitter IDs to collect tweets')
f.close()

#Get Tweets
for twitter_id in all_IDs: 
    
    try:

        log = open('result.log', 'a')

        print('\n')
        print(twitter_id)
        log.write('\n')
        log.write(str(twitter_id) + ':  ')

        #if in prined then skip
        already_pruned = 0
        pruned = open('pruned', 'r')
        for line in pruned:
            if twitter_id == int(line):
                already_pruned = 1
        pruned.close()
        if already_pruned == 1:
            print('      already pruned. Passed.')
            log.write('already pruned.')
            log.close()
            continue

        #if this account is already processed then skip
        if os.path.exists(sys.argv[2]+'/'+str(twitter_id)):
            print('      already processed. Passed.')
            log.write('already processed.')
            log.close()
            continue

        user = api.get_user(twitter_id)

        #prune not interesting IDs
        if user.protected:
            pruned = open('pruned', 'a')
            pruned.write(str(twitter_id) + '\n')
            pruned.close()
            print('      is protected. Passed.')
            log.write('passed.')
            log.close()
            continue

        if not user.geo_enabled:
            pruned = open('pruned', 'a')
            pruned.write(str(twitter_id) + '\n')
            pruned.close()
            print('      is not geo enabled. Passed.')
            log.write('passed.')
            log.close()
            continue
        
        if user.statuses_count < min_status_count:
            pruned = open('pruned', 'a')
            pruned.write(str(twitter_id) + '\n')
            pruned.close()
            print('      does not have enough tweets. Passed.')
            log.write('passed.')
            log.close()
            continue
        
        print('      processing...')

        #Get all the tweets of the twitter_id
        alltweets = []
        new_tweets = api.user_timeline(user_id = twitter_id,count=200)
        alltweets.extend(new_tweets)
        oldest = alltweets[-1].id - 1
        while len(new_tweets) > 0:
            new_tweets = api.user_timeline(user_id = twitter_id, count=200, max_id=oldest)
            alltweets.extend(new_tweets)
            oldest = alltweets[-1].id - 1

        #dump tweets in a single file
        f = open(sys.argv[2]+'/'+str(twitter_id), 'wb')
        pickle.dump(alltweets, f)
        f.close()

        print('  **      successfully processed and its tweets are saved')
        log.write('successfully processed. :D')
        log.close()

    except:
        log.write('EXCEPTION :(')
        log.close()
        print('      EXCEPTION occurred and logged')
        error_logs = open('error.log', 'a')
        error_logs.write(str(twitter_id) + '\n')
        error_logs.close()
        pass

print('\n***************************')
end_time = datetime.now()
print('done at:', end_time.time())
print('script took:', end_time - start_time)


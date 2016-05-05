'''
GET IDs of all followers of a given account and save them into a file 
INPUT Parameters: 
    - Twitter ID to get followers of 
    - File name to pickle dump the result IDs into
'''

import tweepy 
import pickle
import os
import sys
from datetime import datetime
import time

TWEET_PATH = 'Tweets/'
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

#Get followers: 
followers = []
count = 0
for page in tweepy.Cursor(api.followers_ids, screen_name = sys.argv[1]).pages():
    followers.extend(page)
    count = count + len(page)
    print('fetched' , count , 'followers so far.')
    time.sleep(60)

#dump them to file
f = open (sys.argv[2] , 'wb')
pickle.dump(followers, f)
f.close()

end_time = datetime.now()
print('done at:', end_time.time())
print('script took:', end_time - start_time)


'''
INPUT Parameters: 
    - A directory name that contains immigrant objects
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

for immigrant in immigrants: 
    f = open(sys.argv[1] + immigrant, 'rb')
    immigrant_obj = pickle.load(f)
    f.close()

    source_country = immigrant_obj.source_country
    dest_country = immigrant_obj.destination_country
    trip = source_country + ' -> ' + dest_country

    if source_country in src:
        src[source_country] += 1
    else:
        src[source_country] = 1

    if dest_country in dest:
        dest[dest_country] += 1
    else: 
        dest[dest_country] = 1 

    if trip in src_dest:
        src_dest[trip] += 1
    else:
        src_dest[trip] = 1


src = sorted(src.items(), key=operator.itemgetter(1), reverse=True)
f = open('Source.csv', 'w')
for (s, freq) in src:
    f.write(s+','+str(freq)+'\n')
    print(s + ',' + str(freq))
f.close()

dest = sorted(dest.items(), key=operator.itemgetter(1), reverse=True)
f = open('Destination.csv', 'w')
for (d, freq) in dest:
    f.write(d + ',' + str(freq) + '\n')
f.close()

src_dest = sorted(src_dest.items(), key=operator.itemgetter(1), reverse=True)
f = open('Trips.csv', 'w')
for (t, freq) in src_dest:
    f.write(t + ',' + str(freq) + '\n')
f.close()







print('\n***************************')
end_time = datetime.now()
print('done at:', end_time.time())
print('script took:', end_time - start_time)


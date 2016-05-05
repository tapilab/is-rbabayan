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
from scipy.sparse import lil_matrix
from sklearn.cross_validation import KFold
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from collections import Counter
from sklearn.feature_selection import chi2
import numpy as np
import operator


stopwords = [u'i', u'me', u'my', u'myself', u'we', u'our', u'ours', u'ourselves', u'you', u'your', u'yours', u'yourself', u'yourselves', u'he', u'him', u'his', u'himself', u'she', u'her', u'hers', u'herself', u'it', u'its', u'itself', u'they', u'them', u'their', u'theirs', u'themselves', u'what', u'which', u'who', u'whom', u'this', u'that', u'these', u'those', u'am', u'is', u'are', u'was', u'were', u'be', u'been', u'being', u'have', u'has', u'had', u'having', u'do', u'does', u'did', u'doing', u'a', u'an', u'the', u'and', u'but', u'if', u'or', u'because', u'as', u'until', u'while', u'of', u'at', u'by', u'for', u'with', u'about', u'against', u'between', u'into', u'through', u'during', u'before', u'after', u'above', u'below', u'to', u'from', u'up', u'down', u'in', u'out', u'on', u'off', u'over', u'under', u'again', u'further', u'then', u'once', u'here', u'there', u'when', u'where', u'why', u'how', u'all', u'any', u'both', u'each', u'few', u'more', u'most', u'other', u'some', u'such', u'no', u'nor', u'not', u'only', u'own', u'same', u'so', u'than', u'too', u'very', u's', u't', u'can', u'will', u'just', u'don', u'should', u'now']


def tokenize(string, lowercase, keep_punctuation, prefix, collapse_urls, collapse_mentions):
    if not string:
        return []
    if lowercase:
        string = string.lower()
    
    tokens = []
    
    if collapse_urls:
        string = re.sub('http\S+', 'THIS_IS_A_URL', string)
    
    if collapse_mentions:
        string = re.sub('@\S+', 'THIS_IS_A_MENTION', string)
        
    if keep_punctuation:
        tokens = string.split()
    else:
        tokens = re.sub('\W+', ' ', string).split()
        
    if prefix:
        tokens = ['%s%s' % (prefix, t) for t in tokens]
        
    return tokens



def do_vectorize(data, tokenizer_fn=tokenize, min_df=1, max_df=1., binary=True, ngram_range=(1,1)):
    vectorizer = CountVectorizer(input='content', min_df = 2, binary = False, ngram_range = (1,2))
    X = vectorizer.fit_transform(data)
    return X.tocsr(), vectorizer

def select_features(X, y, vec, number_of_features = 100, threshold_rate = 40):
    chi, pvals = chi2(X,y)
    feats = vec.get_feature_names()
    features = {}
    
    rate = threshold_rate
    for i in np.argsort(chi)[::-1]:
        
        #Ignore independet features:
        if chi[i] == 0.00:
            break

#        a = np.where(X[:, i].T.toarray()[0]>=1)
        y = np.array(y)
        #select features that have frequency larger than threshhold rate (set in rate value)
        my_count = Counter(y[np.where(X[:, i].T.toarray()[0]>=1)])
        if my_count[1] > my_count[0] and my_count[0] != 0 and (my_count[1] * 1.0)/my_count[0] > rate:
            feat_rate = (my_count[1] * 1.0)/my_count[0]
            features[feats[i]] = feat_rate

    keywords = [i for i in dict(sorted(features.items(), key=lambda x: x[1]))]
    return keywords[-number_of_features : ]


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


all_tweet_texts = []
labels = [] #0 means before immigration and 1 means after immigration


for immigrant in immigrants: 
    f = open(sys.argv[1] + immigrant, 'rb')
    immigrant_obj = pickle.load(f)
    f.close()

    f = open(sys.argv[2] + immigrant, 'rb')
    tweets = pickle.load(f)
    f.close()

    for tweet in tweets: 
        if tweet.created_at > immigrant_obj.immigration_date: 

            #tweet is made after the immigration:
            text = ' '.join([word for word in tweet.text.split() if word not in stopwords])
            all_tweet_texts.append(text)
            labels.append(1)

        else: 

            #tweet is made before the immigration:
            text = ' '.join([word for word in tweet.text.split() if word not in stopwords])
            all_tweet_texts.append(text)
            labels.append(0)


X, vec = do_vectorize(all_tweet_texts)
features = select_features(X,labels,vec,50)
print(features)

    

print('\n***************************')
end_time = datetime.now()
print('done at:', end_time.time())
print('script took:', end_time - start_time)


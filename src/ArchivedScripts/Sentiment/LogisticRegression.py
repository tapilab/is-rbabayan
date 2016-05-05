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


stopwords = [u'i', u'me', u'my', u'myself', u'we', u'our', u'ours', u'ourselves', u'you', u'your', u'yours', u'yourself', u'yourselves', u'he', u'him', u'his', u'himself', u'she', u'her', u'hers', u'herself', u'it', u'its', u'itself', u'they', u'them', u'their', u'theirs', u'themselves', u'what', u'which', u'who', u'whom', u'this', u'that', u'these', u'those', u'am', u'is', u'are', u'was', u'were', u'be', u'been', u'being', u'have', u'has', u'had', u'having', u'do', u'does', u'did', u'doing', u'a', u'an', u'the', u'and', u'but', u'if', u'or', u'because', u'as', u'until', u'while', u'of', u'at', u'by', u'for', u'with', u'about', u'against', u'between', u'into', u'through', u'during', u'before', u'after', u'above', u'below', u'to', u'from', u'up', u'down', u'in', u'out', u'on', u'off', u'over', u'under', u'again', u'further', u'then', u'once', u'here', u'there', u'when', u'where', u'why', u'how', u'all', u'any', u'both', u'each', u'few', u'more', u'most', u'other', u'some', u'such', u'no', u'nor', u'not', u'only', u'own', u'same', u'so', u'than', u'too', u'very', u's', u't', u'can', u'will', u'just', u'don', u'should', u'now']




class Immigrant(object):
    def __init__(self,user_id, immigration_date,tweets,source_country,destination_country, duration):
        self.user_id = user_id
        self.immigration_date = immigration_date
        self.tweets = tweets
        self.source_country = source_country
        self.destination_country = destination_country
        self.duration = duration


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


def get_words_in_tweets(training):
    all_words = []
    for (words, sentiment) in training:
        all_words.extend(words)
    return all_words

def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features

def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

def extract_train_data(trainings):
    training_text = []
    dejection_labels = []
    
    for train_data in trainings:
        training_text.append(train_data['text'])
        if(train_data['DD'] == 0):
            dejection_labels.append(0)
        else:
            dejection_labels.append(1)
    return training_text,dejection_labels

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


start_time = datetime.now()
print('started at:', datetime.now().time())


#Read Training data into all_trai_data[]
trainings = []
f = open(sys.argv[1], 'r')
for line in f:
    trainings.append(json.loads(line))
f.close()
train_x,train_y = extract_train_data(trainings)
all_train_data = []
for data in train_x:
    text = ' '.join([word for word in data.split() if word not in stopwords])
    all_train_data.append(text)


#print('Now lets create the logistic regression model')   
#X, vec = do_vectorize(all_train_data)
#logistic = LogisticRegression(random_state=42)
#logistic.fit(X, train_y)

#print('lets used the model for immigrants!')

immigrants = os.listdir(sys.argv[2])

output_file = open("logisic_result.csv", "w")

for immigrant in immigrants:

    training_data = copy.deepcopy(all_train_data)

    f = open(sys.argv[2] + immigrant, 'rb')
    immigrant_obj = pickle.load(f)
    f.close()
    
    f = open(sys.argv[3] + immigrant, 'rb')
    tweets = pickle.load(f)
    f.close()
    
    tweets_after = []
    tweets_before = []

    after_no = 0
    before_no = 0
    for tweet in tweets:

        text = ' '.join([word for word in tweet.text.split() if word not in stopwords])

        if tweet.created_at > immigrant_obj.immigration_date:
            tweets_after.append(text)
#            score = logistic.predict_proba(text)
#            logistic_scores_after.append((score[0,0], score[0,1]))
        else:
            tweets_before.append(text)

#    X_after, vec_after = do_vectorize(tweets_after)
#    X_before, vec_before = do_vectorize(tweets_before)

    
    training_size = [i for i in range(len(training_data))]
    training_data.extend(tweets_before)
    testing_before_size = [i for i in range(len(training_size), len(training_data))]
    training_data.extend(tweets_after)
    testing_after_size = [i for i in range(len(training_size) + len(tweets_before), len(training_data))]

    X, vec = do_vectorize(training_data)
    logistic = LogisticRegression()
    logistic.fit(X[training_size], train_y)
   
    testing_size_after = [i for i in range(len(training_data)) if i not in training_size]

    predicted_after = logistic.predict_proba(X[testing_before_size])
    predicted_before = logistic.predict_proba(X[testing_after_size])

    result_after = np.mean(predicted_after, axis = 0)
    result_before = np.mean(predicted_before, axis = 0)

    output_file.write(immigrant+',')
    output_file.write(str(result_before[0])+',')
    output_file.write(str(result_before[1])+',')
    output_file.write(str(result_after[0])+',')
    output_file.write(str(result_after[1])+'\n')

    print(predicted_after)
    print("\n\n\n----------\n\n\n")
    print(predicted_before)

output_file.close()

print('\n***************************')
end_time = datetime.now()
print('done at:', end_time.time())
print('script took:', end_time - start_time)

##Sentiment analysis on immigrant's tweets

###What data will be collected? 

Tweets on twitter related to immigrants.

###How?

For collecting data, I start by crwling users from followers of @USCIS (Official Twitter channel of U.S. Citizenship and Immigration Services) twitter accont.
Users Who have the below features will be consider as immigrants:

1. Users who have tweets in past two years
2. Users who have had a change in their location of the tweets to a location within the United States from another country
3. Users who have tweets from the destination country (USA) for 3 months or more. (The reason that the 3 months period is chosen is becuase of the fact that most of the tourist type visas have a maximum of 3-month length. This would help us to avoid identifyint tourists as immigrants. )

Twitter Stream API will be used to reach the whole timeline of each user.

###How much data?

Optimistically, it would be great if we could identify at least 100 immigrants on Twitter with a similar host country. The number is subject to change in the future while twitter accounts are investigated for recognizing immigrants.

###What are the core research questions?

1. How to identify immigrants on twitter.
2. How much the behaviour of immigrants compared with before immigration. (Happy, Depress)
3. How much the source country and duration of stay have effects on the behaviour of immigrants. 

##What technical methods will be used?

We are facing different type of issues in this topic. 

1. Finding the location of users:
	a) Some of users has public information about their profile user.
	b) If the former method fails, using  the approach discussed in [1].

2. Sentiment analysis on immigrants’ tweets:
	I will mix approaches disscused on [2] and [3] to build a sentiment classifier. Then sentiment analysis will be done using the classifier


###How will it be evaluated?
The evaluation will be done for the sentiment analysis using a classifier evaluator based on the fact the accuracy of the sentiment classifer. 

###Rough timeline (also add milestones)

1. collect data of immigrants from twitter
2. find attributes of each immigrant (source country, host country, duration of stay on host country)
3. build sentiment classifier
4. Sentiment analysis on tweets 
5. Documentation

###References

[1] Zhiyuan Cheng, James Caverlee, Kyumin Lee, “You are where you tweet: a content-based approach to geo-locating Twitter users”, CIKM’10, Toronto, Canada, 2010

[2] Pak, Alexander, and Patrick Paroubek. "Twitter as a Corpus for Sentiment Analysis and Opinion Mining." In LREc, vol. 10, pp. 1320-1326. 2010

[3] Bollen, Johan, Huina Mao, and Xiaojun Zeng. "Twitter mood predicts the stock market." Journal of Computational Science 2, no. 1 (2011): 1-8

#Sentiment analysis on immigrant's tweets

##What data will be collected? 

	Tweets on twitter related to immigrants.

##How?

	Immigrants are those twitter accounts who have had a change in their location of the tweets to a location within the United States from another country. 
	Calculate the duration of residence in the United States. 
	Check for immigrants in past two years. (immigrated in past two years)
	Check users who have tweets in past two years. If they have tweets from the destination country for 3 months or more, consider them as immigrants. We should save that user for sentiment analysis. The reason that the 3 months period is chosen is becuase of the fact that most of the tourist type visas have a maximum of 3-month length. This would help us to avoid identifyint tourists as immigrants. 
	

##How much data?

	Optimistically, it would be great if we could identify at least 100 immigrants on Twitter with a similar host country. The number is subject to change in the future while twitter accounts are investigated for recognizing immigrants.

##What are the core research questions?

	1. How to identify immigrants on twitter.
	2. How much the behaviour of immigrants compared with before immigration. (Happy, Depress)
	3. How much the source country has effects on the behaviour of immigrants. 

##What technical methods will be used?

We are facing different type of issues in this topic. 

	1. Finding the location of users. 
		a. Some of users has public information about their profile user.
		b. If the former method fails, using  the approach discussed in [1]

	2. Sentiment analysis on immigrants’ tweets.
		We will follow the approach discussed in [2] that scores each word in a tweet based on its psychological features such as depression, anxiety, happiness, nervousness, etc. to give a depression rate to each tweet. 


##How will it be evaluated?
	The evaluation will be done for the sentiment analysis using a classifier evaluator based on the fact the accuracy of the sentiment classifer. 

##Rough timeline (also add milestones)

	1. collect raw data from twitter
	2. identify immigrants from raw data
	3. collect tweets of immigrants
	4. find attributes of each immigrant (Source Country, host country)
	5. sentiment analysis on final tweets
	6. Documentation

##References

	[1] Zhiyuan Cheng, James Caverlee, Kyumin Lee, “You are where you tweet: a content-based approach to geo-locating Twitter users”, CIKM’10, Toronto, Canada, 2010
	[2] Jason D. Carr, “Measuring Twitter Sentiment and Implications for Social Psychological Research”, American Journal of Applied Psychology, 2014, Vol. 2, No. 5, 109-113

##Topic: What is the relation between depression and immigration based on users’ tweets

###I splitted the project topic into two major questions:
1. How can we determine if a twitter user is an immigrant in order to build a set of tweets made by immigrants. 
2. How can we determine the sentiment and social behaviour of a particular twitter account based on their tweets to determine if they suffer from a level of depression or not. 

###Related works in regard to finding immigrants on twitter: 

While I have not found a very closely related work that focuses on identifying immigrants on social networks, I could find a set of researches done about geo-locating tweets and web contents based on their textual content. The hope is that the location of the users and the fact that there has been a major change throughout the history of their tweets, might lead us to determine if they have immigrated or not. 

####1. You are where you tweet: A content-based approach to geo-locating twitter users
Authors: Zhiyuan Cheng, James Caverlee, Kyumin Lee 
In the proceedings of 19th ACM international Conference on Information and Knowledge Management, 2010, Toronto 

They successfully estimated the location of 51% of their testing twitter accounts with the precision of up to 100 miles only based on the textual contents of the tweets. Their approach focuses on the keywords used in tweets that might be associated with a certain location, such as a particular expression, a name of a place, or a name of a local event. 


####2. Find me if you can: Improving geographical prediction with social and spatial proximity
Authors: Lars Backstorm, Eric Sun, Cameron Marlow
In the proceedings of World Wide Web Conference, Raleigh, NC

The idea is that the likelihood of friendship with a person decreases with distance, therefore people tend to be located close to their friends. The idea is used in this research to build an algorithm that can anticipate the location of a social network users based on the location of their friends. It is claimed that the proposed algorithm outperforms IP-based geolocation. 


####3. Web-a-Where: Geotagging Web Content
Authors: Einat Amitay, Nadav Har’El, Ron Sivan, Aya Soffer
In the proceedings of the 27th Annual International ACM SIGIR Conference, Sheffield, UK

The goal of this research is to geotag web-pages based on their contents. The approach is to identify keywords in the web-pages that might be associated with different places. However, the challenge targeted in this paper is to resolve ambiguities such as those keywords that might represent different locations, and those that represent both location and non-location meanings. In order to do so, the whole contents of the page is involved in their proposed algorithm to give a score to each potential location for the web-page. 

####4. An Empirical Study of Geographic User Activity Patterns in Foursquare
Authors: Anastasios Noulas, Salvatore Scellato, Cecilia Mascolo, Massimiliano Pontil
Association for the Advancement of Artificial Intelligence, 2011

The research studies users’ activities on Foursquare social network where users are able to check in their locations. The study attempts to identify a correlation between the location of the users and their activities to build a framework for a potential recommendation system. Geolocating the users are solely based on the coordination of the users that they set manually by checking in on the app. This is similar to Twitter’s tweets location. However, Twitter users tend to turn off their location more than Foursquare users. 


####5. Exploring Millions of Footprints in Location Sharing Services
Authors: Zhiyuan Cheng, James Caverlee, Kyumin Lee, Daniel Z. Sui
Association for the Advancement of Artificial Intelligence, 2011

The focus of this research is location based social network such as Foursquare, and Facebook to study the locations of social network users with a goal of building a human mobility pattern. This study also considers the manually set check-ins from the users in social networks for to identify the location of the users. This is how their approach is different from content-based geo-location systems. 

####6. A Tale of Many Cities: Universal Patterns in Human Urban Mobility
Authors:  Anastasios Noulas ,Salvatore Scellato,Renaud Lambiotte,Massimiliano Pontil,Cecilia Mascolo
PloS one 7, no. 5 (2012)

This is yet a another research in shaping human mobility based on their locations on social networks. Again, the locations are based on what the users manually set by checking in on social networks such as Foursquare and Facebook. The result of the paper is a proposed model for human mobility patterns in urban metropolitan cities. 


####7. Geo-Located Tweets. Enhancing Mobility Maps and Capturing Cross-Border Movements
Justine I. Blanford , Zhuojie Huang, Alexander Savelyev, Alan M. MacEachren
PloS one 10, no. 6 (2015)

A very recent study which is somehow closely related to our project in term of identifying cross-border mobility of social network users. The research monitors the
location of users on location based social networks to capture cross border movements. This interests us as we identify such mobilities with some additional constraints as
immigration, and the user would be important for us as an immigrant. Moreover, the research also analyzes twitter accounts and the location of the tweets as well. This
shows some hope that our proposed methodology to identify immigrants on Twitter based on the location of their tweets might work. This research paper needs further careful
study. 


###Related works in regard to identifying social behavioral and psychological features of users on Twitter (Sentiment Analysis on Tweets):

The second problem in this project is to find a methodology to anticipate psychological features of a twitter user, in particular depression. While the goal is for twitter accounts, other proposed approaches that analyzes the sentiment and behaviour of a user based on their web contents might be interested for us as well. Researches done in the fields of Sociology and Psychology are also considered for this purpose. 

####8. Measuring Twitter Sentiment and Implications for Social Psychological Research 
Author: Json D. Carr
American Journal of Applied Psychology, 2014, Vol. 2, No. 5, pp 109-113

The goal of this research is to determine if online tweets represent the idea and opinions of the person who submitted them on twitter. For instance in this research they considered the issue of immigration and concluded that by analyzing the tweets one sent, we are able to determine if they are in favor or opposed to the issue. The analysis and categorizing the tweets however, were done mostly manually to determine if a tweet is positive or negative about the issue. 


####9. Where do my emotions belong? A study of immigrants’ emotional acculturation
Authors: Jozefian De Leersnyder, Batia Mesquita, Heejung S. Kim
Personality and Social Psychology Bulletin 37(4) 451-463

This is another psychological research done manually and based on direct interaction with people and might not be very closely related to our project. Nevertheless, the research revolves around a similar research question as what we are targeting, which is the impact of immigration on one’s psychological feature. The research studied Korean immigrants in the US, and Turkish immigrants in Belgium, with this research assumption that the emotional experiences of people who live together become similar. The result show that an emotional acculturation exist in immigrants. 


####10. Twitter Sentiment Analysis: The Good the Bad and the OMG!
Authors: Efthymios Kouloumpis, Theresa Wilson, Johanna Moore
In the Proceedings of the Fifth International AAAI Conference on Weblogs and Social Media

This is a short paper, but well cited about application of Sentiment Analysis from Natural Language Processing in Twitter. It is argued that previous researches in this regard explored the use of Part-of-Speech features and were not significantly successful due to the incredible breadth of topic that tweets of a user cover. Therefore, they focused on hashtags used in tweets to mine the sentiment of the tweets, besides lexicon, n-gram, and Part-of-Speech features. The combination of all features resulted in the best performance in term of accuracy based on a training data. 


####11. Sentiment Analysis of Twitter Data
Authors: Apoorv Agarwal, Boyi Xie, Illia Vovsha, Owen Rambow, Rebecca Passonneau
In the Proceedings of the Workshop on Language in Social Media (LSM 2011), Portland, Oregon 

This is another research done in sentiment analysis of tweets. The proposed methodology has three major phases; preprocessing, scoring, and design of a Tree Kernel. The preprocessing is done to organize emoticons, URLs, user mentions, and acronyms such as LOL and gr8. The second phase is to score each word based on being positive or negative using a dictionary of 8000 words that are already scored and WordNet. Finally, they build a tree of each tweet and score a tweet based on a large list of proposed features.

####12. Modeling public mood and emotion: Twitter sentiment and socio-economic phenomena
Authors: Bollen, Johan, Huina Mao, and Alberto Pepe.  
ICWSM 11 (2011): 450-453

One of the goal of this paper is to find the mood of tweets. This paper used Profile of 
Mood States psychometric instrument which measures six individual dimensions of 
mood (Tension, Depression, Anger, Vigour, Fatigue, Confusion). After data preparation and 
normalizing tweets, the unit mood vector is produced which shows the total score of each 
tweet based on 6 dimensions.

####13. Twitter as a Corpus for Sentiment Analysis and Opinion Mining
Authors: Pak, Alexander, and Patrick Paroubek 
LREc. Vol. 10. 2010.

The purpose of this paper is to build sentiment classifier, which specifies negative, positive 
and neutral sentiment of texts.  The first step is to collect required corpus. In this paper  tweets are collected with special emoticons. ( “:)” ,“:))”  or  “:(“, ”((“) which show negative and positive sentiment. Then, TreeTagger is used to find POS tags of terms in tweets. After this part they paid attention to the differences between tags distribution. The distribution of POS-tags shows special tags for each positive and negative and neutral sets. Using these information and also construction of n-grams (to handle negation opinion) the sentiment classifier is built using Naive Bayes classifier.	

###Related work on Socialogy:

####14.Immigration and Suicide: the role of marital status, duration of residence, and social integration 
published by PubMed.gov
Authors: Kposowa AJ, McElvain JP, Breault KD.
http://www.ncbi.nlm.nih.gov/pubmed/18240038

This is a related study with a similar-to-ours goal of finding the relation between immigration and psychological features. The research however focuses on the suicide rate of immigrants in California and indicated that the risk of suicide between immigrants is more than twice of the natives. One very interesting parameter that they studies was the duration of residence of the immigrants. The paper argued that the rate of suicide decreases as the duration of residence in the United States increases. This illustrates that the more socially integrated the immigrants become, the less likely it is for them to commit suicide. 
We are able to borrow the idea of studying the duration of residence of the government in our research as well. As long as we identify an immigrant Twitter account, it wouldn’t be too difficult to calculate the duration of their residence in the host country. 

####15. Suicide Rates among Immigrants to the US and in their Former Country
http://suicidemethods.info/tables/immgrant.htm
The data collected by WHO (World Health Statistics Annual) show how the rate of suicide in immigrants have increased for almost every nationality when they moved to the United States. 

####16. Suicide in Canada's immigrant population
Published by PubMed.gov
Author: Malenfant EC
http://www.ncbi.nlm.nih.gov/pubmed/15151027

The study argues that the suicide rate in immigrants to Canada have generally increased compared with the suicide rate in their home country. The result suggests that the immigration has probably caused depression, and anxiety. 

####17. Suicide in Immigrants: An Overview
Open Journal of Medical Psychology, 2013, 2, 124-133 
Authors: Katarzyna Anna Ratkowska, Diego De Leo
http://dx.doi.org/10.4236/ojmp.2013.23019

This paper investigates the rate of suicide and the complexity of several parameters impacting the fact that immigration has increased the rate of suicide. Globalization, acculturation and acculturation stress, genetic and environmental factors, urbanization and ethnic density, first or second generation of immigrants, being in adolescents, and being a refugee and asylum seeker, are among the primary parameters discussed in this research that might be the cause of increased suicide and depression rate between immigrants. 


####18. The Influences of Place of Birth and Socioeconomic Factors on Attempted Suicide in a Defined Population of 4.5 Million People
Jeanette Westman, Jan Hasselström, Sven-Erik Johansson, Jan Sundquist
http://archpsyc.jamanetwork.com/article.aspx?articleid=207351&resultClick=3

The research categorized the suicides attempts in Sweden based on the place of birth and gender of the person who attempted the suicide. We divided the number of attempted suicides to the total population of immigrants for each home country in Sweden, to calculate the rate of suicides for in immigrants based on their home country. The result illustrated that the suicide rate for immigrants from almost every country is more than the native swedish people. For example the suicide rate of Iranian immigrants in Sweden is twice more than the rate of native people of Sweden, in spite of the fact that the suicide rate of native Iranians living in Iran is half the suicide rate of people from Sweden. 

####19. Migration from Mexico to the United States and Subsequent Risk for Depressive and Anxiety Disorders
Authors: Stephanie R. Potochnick, Krista M. Perreira
http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3139460/

The research actively monitored the psychological features of more than 500 Mexican immigrants in the United States and concluded that “After arrival in the United States, migrants had a significantly higher risk for first onset of any depressive or anxiety disorder than did non-immigrant family members of migrants in Mexico.” 


###Conclusion of the week (1/18/2016)

In conclusion, I feel a bit more comfortable about finding a methodology for sentiment analysis of tweets in order to identify depression in Twitter accounts. However, my major concern is about the first research question on how to recognize immigrants on Twitter. 

###Conclusion of the week (2/1/2016)

####Related to Socialogy and Project Assumption:

Based on socialogy research poper I formed the primary research assumptions:

	- There is a direct correlation between immigration and psychological features of the immigrants. 
	- It is more likely for immigrants to develop psychological disorders than the native people of a country. 
	- Immigrants tend to have a higher rate of anxiety and depression compared to the people of their home country who have not migrated anywhere. 
	- The duration of the residence of the immigrants in the newer country will decrease the chance of developing a psychological disorder. 

Moreover, the literature review gave me the idea of investigating immigrants’ duration of residence in the new country as one of the parameters in my research project. 

In a nutshell, the conclusion is that I will focus on the United States as the host country primarily for the following reasons:

	- Large number of supporting researches and data 
	- English speaking country would help find English tweets 
	- Large number of immigrants every year with diverse countries of origins 

Then the immigrants will be categorized based on their country of origin and the duration of their residence in the United States. The sentiment analysis would be the next phase to detect psychological features before and after the immigration. 

####Related to Sentiment Analysis:

Based on two papers that I found [12] and [13], I built the first idea to produce sentiment 
classifier. The POMS can be used to create the very first sets of moods and then 
TreeTagger can be generated POS-tags of these sets to find the distribution of mood if 
tweets based on POS-tags. At the end sentiment classifier is produced by using Naive 
Bayes classifier.




	

	


1/18/2016

Topic: What is the relation between depression and immigration based on users’ tweets

I splitted the project topic into two major questions:
How can we determine if a twitter user is an immigrant in order to build a set of tweets made by immigrants. 
How can we determine the sentiment and social behaviour of a particular twitter account based on their tweets to determine if they suffer from a level of depression or not. 

Related works in regard to finding immigrants on twitter: 

While I have not found a very closely related work that focuses on identifying immigrants on social networks, I could find a set of researches done about geo-locating tweets and web contents based on their textual content. The hope is that the location of the users and the fact that there has been a major change throughout the history of their tweets, might lead us to determine if they have immigrated or not. 

1.You are where you tweet: A content-based approach to geo-locating twitter users
Authors: Zhiyuan Cheng, James Caverlee, Kyumin Lee 
In the proceedings of 19th ACM international Conference on Information and Knowledge Management, 2010, Toronto 

They successfully estimated the location of 51% of their testing twitter accounts with the precision of up to 100 miles only based on the textual contents of the tweets. Their approach focuses on the keywords used in tweets that might be associated with a certain location, such as a particular expression, a name of a place, or a name of a local event. 


2.Find me if you can: Improving geographical prediction with social and spatial proximity 
Authors: Lars Backstorm, Eric Sun, Cameron Marlow
In the proceedings of World Wide Web Conference, Raleigh, NC

The idea is that the likelihood of friendship with a person decreases with distance, therefore people tend to be located close to their friends. The idea is used in this research to build an algorithm that can anticipate the location of a social network users based on the location of their friends. It is claimed that the proposed algorithm outperforms IP-based geolocation. 


3.Web-a-Where: Geotagging Web Content 
Authors: Einat Amitay, Nadav Har’El, Ron Sivan, Aya Soffer
In the proceedings of the 27th Annual International ACM SIGIR Conference, Sheffield, UK

The goal of this research is to geotag web-pages based on their contents. The approach is to identify keywords in the web-pages that might be associated with different places. However, the challenge targeted in this paper is to resolve ambiguities such as those keywords that might represent different locations, and those that represent both location and non-location meanings. In order to do so, the whole contents of the page is involved in their proposed algorithm to give a score to each potential location for the web-page. 


Related works in regard to identifying social behavioral and psychological features of users on Twitter:

The second problem in this project is to find a methodology to anticipate psychological features of a twitter user, in particular depression. While the goal is for twitter accounts, other proposed approaches that analyzes the sentiment and behaviour of a user based on their web contents might be interested for us as well. Researches done in the fields of Sociology and Psychology are also considered for this purpose. 

4.Measuring Twitter Sentiment and Implications for Social Psychological Research 
Author: Json D. Carr
American Journal of Applied Psychology, 2014, Vol. 2, No. 5, pp 109-113

The goal of this research is to determine if online tweets represent the idea and opinions of the person who submitted them on twitter. For instance in this research they considered the issue of immigration and concluded that by analyzing the tweets one sent, we are able to determine if they are in favor or opposed to the issue. The analysis and categorizing the tweets however, were done mostly manually to determine if a tweet is positive or negative about the issue. 


5.Where do my emotions belong? A study of immigrants’ emotional acculturation 
Authors: Jozefian De Leersnyder, Batia Mesquita, Heejung S. Kim
Personality and Social Psychology Bulletin 37(4) 451-463

This is another psychological research done manually and based on direct interaction with people and might not be very closely related to our project. Nevertheless, the research revolves around a similar research question as what we are targeting, which is the impact of immigration on one’s psychological feature. The research studied Korean immigrants in the US, and Turkish immigrants in Belgium, with this research assumption that the emotional experiences of people who live together become similar. The result show that an emotional acculturation exist in immigrants. 


6.Twitter Sentiment Analysis: The Good the Bad and the OMG!
Authors: Efthymios Kouloumpis, Theresa Wilson, Johanna Moore
In the Proceedings of the Fifth International AAAI Conference on Weblogs and Social Media

This is a short paper, but well cited about application of Sentiment Analysis from Natural Language Processing in Twitter. It is argued that previous researches in this regard explored the use of Part-of-Speech features and were not significantly successful due to the incredible breadth of topic that tweets of a user cover. Therefore, they focused on hashtags used in tweets to mine the sentiment of the tweets, besides lexicon, n-gram, and Part-of-Speech features. The combination of all features resulted in the best performance in term of accuracy based on a training data. 


7.Sentiment Analysis of Twitter Data
Authors: Apoorv Agarwal, Boyi Xie, Illia Vovsha, Owen Rambow, Rebecca Passonneau
In the Proceedings of the Workshop on Language in Social Media (LSM 2011), Portland, Oregon 

This is another research done in sentiment analysis of tweets. The proposed methodology has three major phases; preprocessing, scoring, and design of a Tree Kernel. The preprocessing is done to organize emoticons, URLs, user mentions, and acronyms such as LOL and gr8. The second phase is to score each word based on being positive or negative using a dictionary of 8000 words that are already scored and WordNet. Finally, they build a tree of each tweet and score a tweet based on a large list of proposed features.


Conclusion of the week

In conclusion, I feel a bit more comfortable about finding a methodology for sentiment analysis of tweets in order to identify depression in Twitter accounts. However, my major concern is about the first research question on how to recognize immigrants on Twitter. 

### Measuring the effect of immigration on mood expressed on Twitter
======


Traditional studies in Social Science and Psychology indicated a higher risk of depression and mood change in immigrants after their immigration. This project studies the impact of immigration on people based on their mood expressed in their tweets on Twitter. The project has two major parts; 1) identifying the immigrants on Twitter and 2) analyze the sentiment of their tweets to study their mood. For the first part we relied on Twitter geo-location meta-data to see if a user has moved from a country to another. And for the second part we built a Logistic Regression classifier that could assign a probability value to each tweet for three trained class labels; anxiety, dejection, and hostility. The results indicate that all class labels generally increase after immigration in our set of identified immigrants.

#### Data and Folder Structure

The report shows the result of analyzing more than 22,000 users in which around 1000 immigrants oare identified. This is around 120GB of data. As a proof of the concept a small dataset of 5 users with their tweets are checked in here. The full dataset is stored on TAPILab server. Here are where all the data are stored on TAPILab server and their equivalent sample on this repository: 

1. All Collected tweets of all user accounts
  * TAPI Server: /data/2/rbabayan/Tweets
  * Source Control: /src/MetaFiles/Tweets

2. Identified Immigrantss: 
  * TAPI Server: /home/rbabayan/ms-project/Code/Filtering/Immigrants
  * Source Control: /src/MetaFiles/Immigrants
  
3. Immigrant Objects for the Identified Immigrantss: 
  * TAPI Server: /home/rbabayan/ms-project/Code/Filtering/Immigrants
  * Source Control: /src/MetaFiles/ImmigrantsObjects
  
4. Features (gender, rate of tweets, etc) for the Identified Immigrantss: 
  * TAPI Server: /home/rbabayan/ms-project/Code/DiffInDiff/ImmigrantsFeatures
  * Source Control: /src/MetaFiles/ImmigrantsFeatures
  
5. Features (gender, rate of tweets, etc) for the Identified Immigrantss: 
  * TAPI Server: /home/rbabayan/ms-project/Code/DiffInDiff/ImmigrantsFeatures
  * Source Control: /src/MetaFiles/ImmigrantsFeatures

6. Trainind Data: 
  * TAPI Server: /home/rbabayan/ms-project/Code/Sentiment/3K-labeled
  * Source Control: /src/MetaFiles/3K-labeled
  
7. Identified non-immigrant Similar Accounts:
  * TAPI Server: /home/rbabayan/ms-project/Code/DiffInDiff/CandidatesPerImmigrant/similars.csv
  * Source Control: /src/MetaFiles/similars.csv

#### Code

The source code of the project including; 
  * Collecting data
  * Identifying immigrants
  * Get immigrants features
  * Build the sentiment analysis classifier 
  * Analyze the sentiment of the tweets
  * Find similar non-immigrant users for every immigrant
  * Difference in Differences analysis
  * Plotting the results 

are stored in /src/Final Code/Code.ipynb in form of a notebook Python3 file. 

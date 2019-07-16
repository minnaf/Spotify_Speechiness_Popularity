# mod3project


By: Minna Fingerhood, Dustin Breitner


Question for this project: What is speechiness and does it have an effect on popularity? 

A)Does speechiness have an affect on a song's popularity?
   H0: Speechiness has no effect on a song's popularity
   HA: Speechiness has an effect on a song's popularity    
                
B)How does speechiness affect a song's popularity within a certain genre?
   H0: Speechiness has no effect on a song's popularity 
   HA: Speechiness has an effect on a song's popularity
    
   H0: Genre has no effect on a song's popularity
   HA: Genre has an effect on a song's popularity
   
   H0: There is no interaction beween speechiness and genre
   HA: There is an interaction between speechiness and genre
           
C)How does speechiness affect a song's popularity within a certain country?
   H0: Speechiness has no effect on popularity 
   HA: Speechiness has an effect on popularity
    
   H0: Country has no effect on popularity
   HA: Country has an effect on popularity
   
   H0: There is no interaction betwen speechiness and country
   HA: There is an interaction between speechiness and country
 
----------------------

Outline of Project:

1. Gather playlist data from Spotify API and put in SQL database
2. Gather song data from Spotify API using song_ids in the playlist and put into SQL table
3. Create Pandas DataFrame 
4. Perform data analysis on all three of our questions
5. Interpret results 

-------------------


1. To gather playlist data from the Spotify API, we used requests.get(). Spotify's API documentation requies an OAuth Token and playlist_ID, which gathered from spotify's developer website and app. 
We retrieved this data and subsequently organized it by isolating categories of (1) song name, (2) song_id, (3) popularity and (4) artist_name into a SQL database. 

2. Using the column in our SQL table, 'song_id,' we retrieved audio features of the tracks which included information such as:  "danceability," "energy," "key," "loudness," "mode," "speechiness," "acousticness," "instrumentalness," "liveness," "valence," and "tempo." We extracted danceability, speechiness, liveness, valence, and energy and inputted it into our SQL table. Then, we converted to pandas dataframe for greate accessibility. Because we are primarily analyzing speechiness, the provided definition from Spotify's API is as follows: "Speechiness detects the presence of spoken words in a track. The more exclusively speech-like the recording (e.g. talk show, audio book, poetry), the closer to 1.0 the attribute value. Values above 0.66 describe tracks that are probably made entirely of spoken words. Values between 0.33 and 0.66 describe tracks that may contain both music and speech, either in sections or layered, including such cases as rap music. Values below 0.33 most likely represent music and other non-speech-like tracks."

3. After inputting our data into different SQL tables, we converted each table to a Pandas Dataframe and made a new column for genre (or country, depending on the question), then  combined all the tables. We also made another column, "speechiness_binned" that categorized the speechiness data so that we could have discrete data for our 2-way ANOVA test. In this category, 0 is the least speechiness and 9 is the highest speechiness. We also dropped all rows with null values. This decreased our sample size dramatically because audio features are relatively new and therefore only available for newer tracks.

4. Once we had all of our data, we created a distribution plot of popularity (our dependent variable) to see if it was normally distributed. Our data is left skewed, as demonstrated by the distribution. We chose not to normalize our data set because we only want to analyze our results, we do not want to predict results... Therefore, normalization is not as important. 

(A) Q: Does speechiness have an effect on popularity? 
    A: Speechiness has an effect on a song's popularity 
    Method: We vizualized our data with a scatter plot and ran the pearson correlation test. We received an R value of 0.14412568748741614 with a p-value of 0.0029345405599397406, which indicates a small relationship between popularity and speechiness, so we can therefore reject the null hypothesis.  
    
(B) Q: How does speechiness affect a song's popularity within a certain genre?
    A: 1. Speechiness has no effect on a song's popularity
       2. Genre has an effect on a song's popularity
       3. There is no interaction beween speechiness and genre
    Method: We ran an ols model where our dependent variable was popularity and our independent variables were genre and speechiness_binned (both categorical). We got a F-statistic of 5.914 for the entire model and a p-value of 0.0000, leading us to concude that the relationship between popularity and speechiness/genre was signficant. We then ran a 2-way ANOVA test and found that the F-statistic for popularity and speechiness_binned was 2.089811 and the F-statistic for popularity and genre was 45.502033. Therefore, both these features have variance from mean to mean. We also found the interaction factor between genre and to have an F-value close of 0.705180 with a p-value of 0.08%, which led us to fail to reject the null hypothesis for interaction. 
    We followed the ANOVA test with a tukeys range test to see which features specifically influenced popularity. Our results indicate that we can reject the null hypothesis for genre's affect on popularity. However, our sample size is rather large so we have a higher probability of committing a type I error. We think this occurred in the case of popularity ~ speechiness, because when we ran our tukeys test, we received all false values. Additionally, our  F-statistic in the ANOVA test was 2.089811 and the p-value was 0.02, which is not indicating much confidence below our alpha of 0.05 (which is standard for this kind of data). 
    
    
(C) Q: How does speechiness affect a song's popularity within a certain country?
    A: 1. Speechiness has an effect on popularity
       2. Country has an effect on popularity
       3. There is no interaction betwen speechiness and country
    Method: Similar to the method for question (B), we gathered data by country and created an ols model where popularity was the dependent variable and speechiness and country were the independent variables. We found the F-statistic for the entire model to be 1.645 with a  p- value of 0.0062. Therefore we rejected the null hypothesis. When we ran the 2-way ANOVA test we failed to reject the null hypothesis for interaction because the p-value was 0.683894, but rejected the null hypothesis for speechiness's effect on popularity and countries effect on popularity because the p values were less than 0.05. When we ran tukeys range test for both features we found that for countries, Brazil and Australia, were the only two groups that have a significant difference. Further, when we ran the tukeys for speechiness, we found significant differences between groups 1 and 2, 2 and 4, 4 and 6. This means that popularity differed significantly for popularity between those two countries and that speechiness had an effect on popularity between the three paired groups. 
    
  






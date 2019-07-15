# mod3project


By: Minna Fingerhood, Dustin Breitner 


Questions for this project: 

1)Does speechiness have an affect on a song's popularity?
   H0: Speechiness has no effect on a song's popularity
   HA: Speechiness has an effect on a song's popularity    
                
2)How does speechiness affect a song's popularity within a certain genre?
   H0: Speechiness has no effect on a song's popularity 
   HA: Speechiness has an effect on a song's popularity
    
   H0: Genre has no effect on a song's popularity
   HA: Genre has an effect on a song's popularity
   
   H0: There is no interaction beween speechiness and genre
   HA: There is an interaction between speechiness and genre
           
3)How does speechiness affect a song's popularity within a certain country?
   H0: Speechiness has no effect on popularity 
   HA: Speechiness has an effect on popularity
    
   H0: Country has no effect on popularity
   HA: Country has an effect on popularity
 

----------------------

Outline of Project:

1. Gather playlist data from Spotify API and put in SQL database
2. Gather song data from Spotify API using song_ids in the playlist and put into SQL table
3. Create Pandas DataFrame 
4. 
5. 
-------------------


1. To gather playlist data from the Spotify API, we used requests.get(). Spotify's API documentation requies an OAuth Token and playlist_ID, which gathered from spotify's developer website and app. 
We retrieved this data and subsequently organized it by isolating categories of (1) song name, (2) song_id, (3) popularity and (4) artist_name into a SQL database. 

2. Using the column in our SQL table, 'song_id,' we retrieved audio features of the tracks which included information such as:  "danceability," "energy," "key," "loudness," "mode," "speechiness," "acousticness," "instrumentalness," "liveness," "valence," and "tempo." We extracted danceability and speechiness and inputted it into our SQL table. Then, we converted to pandas dataframe for greate accessibility. 

3. Create a pandas data frame using this data 

4. 







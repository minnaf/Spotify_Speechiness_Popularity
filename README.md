# mod3project


By: Minna Fingerhood, Dustin Breitner 


Goals of this project: 

1. 
2. 
3. 

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


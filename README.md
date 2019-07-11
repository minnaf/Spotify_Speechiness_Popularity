# mod3project


By: Minna Fingerhood, Dustin Breitner 


Goals of this project: 

1. 
2. 
3. 

----------------------

Outline of Project:

1. Gather playlist data from Spotify API 
2. Gather song data from Spotify API using song_ids in the playlist
3. Create SQL database and tables of the data
4. Organize the data 
5. 
-------------------


1. To gather playlist data from the Spotify API, we used requests.get(). Spotify's API documentation requies an OAuth Token and playlist_ID, which gathered from spotify's developer website and app. 
We retrieved this data and subsequently organized it by isolating categories of (1) song name, (2) song_id, (3) popularity and (4) artist_name. We then converted this information into a pandas DF for easier comprehension and accessibility. 

2. Using the column, 'song_id,' we retrieved audio features of the tracks which included information such as:  "danceability," "energy," "key," "loudness," "mode," "speechiness," "acousticness," "instrumentalness," "liveness," "valence," and "tempo." 


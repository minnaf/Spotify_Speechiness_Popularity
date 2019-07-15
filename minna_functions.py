import requests
import json
import pandas as pd 
import numpy as np
import sqlite3
import math

conn = sqlite3.connect('spotify.db')
c = conn.cursor()


class get_spotify_playlist():
    
    def __init__(self, OAuth_token):
        self.headers_value = OAuth_token
        self.headers = {'Authorization':f'Bearer {self.headers_value}'}
        
    def get_playlist_SQL(self, playlist_id, table_name):
        '''takes in playlist_id and pulls from API, and returns SQL database '''
        resp = requests.get(f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks?offset=0&limit=100', headers = self.headers)
        data_json = resp.json()
        #return data_json
        
        c = conn.cursor()
        c.execute(f'''CREATE TABLE IF NOT EXISTS {table_name}
                 ([index] INTEGER PRIMARY KEY,
                 [song_name] text, 
                 [song_id] text,
                 [popularity] integer,
                 [artist_name] text,
                 [speechiness] float, 
                 [danceability] float, 
                 [energy] float,
                 [liveness] float, 
                 [valence] float)''')

        
        for i in data_json['items']:  
            c.execute(f'''INSERT INTO {table_name} 
                    (song_name, song_id, popularity, artist_name)
                    VALUES(?,?,?,?)''', 
                    (i['track']['name'],
                     i['track']['id'],
                     i['track']['popularity'],
                     i['track']['artists'][0]['name']))
    
            conn.commit()
         
        c.execute(f'SELECT * FROM {table_name}')
        
        
        c.fetchall()

                
    @staticmethod
    def SQL_to_dataframe(table_name):
        '''takes in SQL table_name and converts to pandas dataframe, returning the head of the dataframe'''
        df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn, index_col='index')
        df = df.drop_duplicates() 
        return df    
   

    def song_audio_features(self, df, table_name):
        '''takes in dataframe table and corresponding SQL table and returns dataframe with audio features for the songs'''
       
        song_ids = list(df['song_id'])
        for i in range(0, math.ceil(len(song_ids)/100)):
            abbr_list = song_ids[i:i+100]    
            
            formatted = (",".join(abbr_list))
            resp = requests.get(f'https://api.spotify.com/v1/audio-features?ids={formatted}', headers = self.headers)
            data_json = resp.json()
            
            for j in data_json['audio_features']:
                try:
                    c.execute(f'''UPDATE {table_name} 
                                  SET speechiness = ?, 
                                      danceability = ?, 
                                      energy = ?,
                                      liveness = ?,
                                      valence = ?
                                  WHERE song_id = ?''', (j['speechiness'], j['danceability'], j['energy'], j['liveness'], j['valence'], j['id'],))
                    conn.commit()
                except:
                    print(j)
         
        return get_spotify_playlist.SQL_to_dataframe(f'{table_name}')
        
       
            
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

   
        
      
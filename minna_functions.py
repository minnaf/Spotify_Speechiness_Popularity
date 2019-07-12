import requests
import json
import pandas as pd 
import sqlite3

conn = sqlite3.connect('spotify.db')
c = conn.cursor()


class get_spotify_playlist():
    
    def __init__(self, OAuth_token):
        self.headers_value = OAuth_token
        self.headers = {'Authorization':f'Bearer {self.headers_value}'}
        
    def get_playlist_SQL(self, playlist_id, table_name):
        '''takes in playlist_id and pulls from API, and returns SQL database '''
        #headers_value = OAuth_token
        #headers = 
        resp = requests.get(f'https://api.spotify.com/v1/playlists/{playlist_id}', headers = self.headers)
        data_json = resp.json()
        
        
        c = conn.cursor()
        c.execute(f'''CREATE TABLE IF NOT EXISTS {table_name}
                 ([id] INTEGER PRIMARY KEY,
                 [song_name] text, 
                 [song_id] text,
                 [popularity] integer,
                 [artist_name] text,
                 [speechiness] float, 
                 [danceability] float)''')

        
        for i in data_json['tracks']['items']:  
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
        df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn, index_col='id')
        return df    
   

    def song_audio_features(self, df, table_name):
        '''takes in dataframe table and corresponding SQL table and returns dataframe with audio features for the songs'''
       
        song_ids = list(df['song_id'])
        
        
        if len(song_ids) < 100:
            formatted = (",".join(song_ids))
            resp = requests.get(f'https://api.spotify.com/v1/audio-features?ids={formatted}', headers = self.headers)
            data_json = resp.json()
            
            for i in data_json['audio_features']:
                c.execute(f'''UPDATE {table_name} 
                              SET speechiness = ?, 
                                  danceability = ?
                              WHERE song_id = ?''', (i['speechiness'], i['danceability'], i['id']))
                conn.commit()
         
            return get_spotify_playlist.SQL_to_dataframe(f'{table_name}')
        
        
        else:
            return 'length of song_ids is > 100, has to be divided' 
            
            
class statistics(): 
    pass
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

   
        
      
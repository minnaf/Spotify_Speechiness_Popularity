import requests
import json
import pandas as pd 
import sqlite3

conn = sqlite3.connect('spotify.db')

class get_spotify_playlist():
        
    def get_playlist_SQL(self, playlist_id, OAuth_token, table_name):
        '''takes in playlist_id and OAuth token from spotify API, pulls from API, and returns SQL database '''
        headers_value = OAuth_token
        headers = {'Authorization':f'Bearer {headers_value}'}
        resp = requests.get(f'https://api.spotify.com/v1/playlists/{playlist_id}', headers = headers)
        
        #name_id_df = pd.DataFrame(columns = ['song_name', 'song_id'])
        
        c = conn.cursor()
        c.execute(f'''CREATE TABLE IF NOT EXISTS {table_name}
                 ([generated_id] INTEGER PRIMARY KEY,
                 [song_name] text, 
                 [song_id] text,
                 [popularity] integer,
                 [artist_name] text)''')

        
        for i in range(len(resp.json()['tracks']['items'])):  
            c.execute(f'''INSERT INTO {table_name} 
                    ([song_name], song_id, popularity, artist_name)
                    VALUES(?,?,?,?)''', 
                    (resp.json()['tracks']['items'][i]['track']['name'],
                     resp.json()['tracks']['items'][i]['track']['id'],
                     resp.json()['tracks']['items'][i]['track']['popularity'],
                     resp.json()['tracks']['items'][i]['track']['artists'][0]['name']))
    
            conn.commit()
         
        c.execute(f'SELECT * FROM {table_name}')
        
        
        c.fetchall()
#         c.close()
#         conn.close()
                
        
    def SQL_to_dataframe(self, table_name):
        '''takes in SQL table_name and converts to pandas dataframe, returning the head of the dataframe'''
        df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
        return df    
   

 class get_spotify_songs(): 
        
        def __init__(self, song_ids):
            self.song_ids = 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

   
        
      
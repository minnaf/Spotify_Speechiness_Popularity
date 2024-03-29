import requests
import json
import pandas as pd 
import sqlite3

conn = sqlite3.connect('spotify2.db')
c = conn.cursor()


class get_spotify_playlist():
    
    def __init__(self, OAuth_token):
        self.headers_value = OAuth_token
        self.headers = {'Authorization':f'Bearer {self.headers_value}'}
        
    def get_album_SQL(self, album_id, table_name):
        '''takes in playlist_id and pulls from API, and returns SQL database '''
        #headers_value = OAuth_token
        #headers = 
        resp = requests.get(f'https://api.spotify.com/v1/albums/{album_id}/tracks', headers = self.headers)
        data_json = resp.json()
        
        
        c = conn.cursor()
        c.execute(f'''CREATE TABLE IF NOT EXISTS {table_name}
                 ([index] INTEGER PRIMARY KEY,
                 [song_name] text, 
                 [song_id] text,
                 [popularity] integer,
                 [artist_name] text,
                 [speechiness] float, 
                 [danceability] float)''')

        
        for i in data_json['items']:  
            c.execute(f'''INSERT INTO {table_name} 
                    (song_name, song_id, popularity, artist_name)
                    VALUES(?,?,?,?)''', 
                    (i['name'],
                     i['id'],
                     i['track']['popularity'],
                     i['track']['artists'][0]['name']))
    
            conn.commit()
         
        c.execute(f'SELECT * FROM {table_name}')
        
        
        c.fetchall()

                
    @staticmethod
    def SQL_to_dataframe(table_name):
        '''takes in SQL table_name and converts to pandas dataframe, returning the head of the dataframe'''
        df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn, index_col='index')
        return df    
   

    def song_audio_features(self, df, table_name):
        '''takes in dataframe table and corresponding SQL table and returns dataframe with audio features for the songs'''
       
        song_ids = list(df['song_id'])
        
        
        #if len(song_ids) < 100:
        for i in range(0, (len(song_ids) // 100)):
            abbr_list = song_ids[i:i+100]    
            
            formatted = (",".join(abbr_list))
            resp = requests.get(f'https://api.spotify.com/v1/audio-features?ids={formatted}', headers = self.headers)
            data_json = resp.json()
            #print(data_json)
            for i in data_json['audio_features']:
                #print(i['speechiness'], i['danceability'], i['id'])
                try:
                    c.execute(f'''UPDATE {table_name} 
                                  SET speechiness = ?, 
                                      danceability = ?
                                  WHERE song_id = ?''', (i['speechiness'], i['danceability'], i['id']))
                    conn.commit()
                except:
                    print(i)
         
        return get_spotify_playlist.SQL_to_dataframe(f'{table_name}')
        
        
        else:
            return 'length of song_ids is > 100, has to be divided' 
            
            
class statistics(): 
    pass
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

   
        
      
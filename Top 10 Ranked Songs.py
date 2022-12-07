'''
https://platform.stratascratch.com/coding/9995-top-10-ranked-songs?code_type=2

Find the top 10 ranked songs by position. 
Output the track name along with the corresponding position and 
sort records by the position in descending order and track name alphabetically, 
as there are many tracks that are tied for the same position.
'''

import pandas as pd

# spotify_worldwide_daily_song_ranking.head()
top_ten=spotify_worldwide_daily_song_ranking
# print(top_ten.columns)

top_ten.drop(top_ten[top_ten['position'] > 10].index,inplace=True)
top_ten=top_ten.sort_values(['position','trackname'],ascending=[False,True])
top_ten[['trackname','position']]

# this tells us that there are some positions that have no songs
# print(pd.unique(df1['position']))
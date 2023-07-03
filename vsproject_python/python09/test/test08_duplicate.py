import numpy as np
import pandas as pd

df_bb = pd.read_csv('./data/billboard.csv')
# print(df_bb)

df_bb_long = df_bb.melt(id_vars=['year', 'artist', 'track', 'time', 'date.entered'])
# print(df_bb_long)
# print(df_bb_long.columns)
df_song = df_bb_long[['year', 'artist', 'track', 'time']]   # 중복된 데이터 저장
df_artist = df_song['artist']
# print(df_artist.shape[0])
# print(df_song)
# print(df_song.shape[0])

# df_duplicate = df_bb_long[df_bb_long['track']=='Loser']
# print(df_duplicate)
# print(df_duplicate.shape[0])

# df_song_remove = df_song.drop_duplicates()
# print(df_song_remove)

df_artist = df_artist.drop_duplicates()
print(df_artist.shape[0])
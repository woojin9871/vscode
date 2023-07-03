'''
    2번에서 가져온 datetime 데이터에서 
    월 데이터가 03인 데이터만 가져와서 출력하시오
'''
from datetime import datetime
import pandas as pd

df = pd.read_csv('./data/COVID19.csv')
# print(df)

df_time = df['시점']
# print(df_time)
 
df_dttm = pd.to_datetime(df_time)
# print(df_dttm)

# df['시점'] = pd.to_datetime(df['시점']).fillna(0)
# dfm = df[df['시점'].dt.month == 5]
# print(dfm)


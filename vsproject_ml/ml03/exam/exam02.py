'''
    ./data/COVID19.csv
    여기에 시점이라는 날짜데이터가 있는데
    datetime 형식으로 변환해서 출력하시오
'''
from datetime import datetime
import pandas as pd

df = pd.read_csv('./data/COVID19.csv')
print(df)

df_time = df['시점'].head(n=5)
print(df_time)
 
df_dttm = pd.to_datetime(df_time)
print(df_dttm)
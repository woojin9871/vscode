from datetime import datetime
import pandas as pd

df_time = pd.read_csv('./data/country_timeseries.csv')
# print(df_time.head(n=5))

# Date 컬럼의 문자열을 => datetime 변환하기 to_datetime()
# print(df_time['Date'].head(n=5))

# 새로운 컬럼을 만들어서 datetime 형식으로 추가하기
df_time['dttm'] = pd.to_datetime(df_time['Date'])
print(df_time.info())






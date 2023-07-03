from datetime import datetime
import pandas as pd

df_time = pd.read_csv('./data/country_timeseries.csv', parse_dates=['Date'])
# print(df_time['Date'].head(n=5))    # 이미dttm 형식 변환 됨

df_time['yyyy'] = df_time['Date'].dt.year
df_time['mm'] = (df_time['Date'].dt.month)
print(df_time[['yyyy', 'mm']].head(n=5))    # 이미 dttm 형식 변환 됨
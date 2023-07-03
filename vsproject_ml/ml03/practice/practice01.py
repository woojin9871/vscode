from datetime import datetime
import pandas as pd

df_time = pd.read_csv('./data/country_timeseries.csv')
# print(df_time.iloc[-5:, :7])

df_time['date_dt'] = pd.to_datetime(df_time['Date'])
# print(df_time[['Date', 'date_dt']].head(n=10))
print('최초발생일자 : ', df_time['date_dt'].min())
print('최근발생일자 : ', df_time['date_dt'].max())

# 진행 과정의 날수 계산
df_time['outbreak_day'] = (df_time['date_dt'] - df_time['date_dt'].min())
print(df_time[['date_dt', 'outbreak_day']])

# 2014 데이터만 추출해서
# 진행날짜수를 출력하시오

df_time_2014 = df_time[df_time['date_dt'].dt.year == 2014]

df_time_2014['outbreak_day'] = (df_time_2014['date_dt'] - df_time_2014['date_dt'].min())
print(df_time_2014[['date_dt', 'outbreak_day']])

# df_2014 = df_time[df_time['Date'].str.contains('2014')]
# print(df_2014[['date_dt', 'outbreak_day']])



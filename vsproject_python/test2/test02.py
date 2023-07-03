'''
    지하철 열차 승하차 데이터를 사용하여 퇴근시간 (17시~19시) 에
    가정 혼잡한 역을 출력하시오
    https://www.data.go.kr/
    서울교통공사_역별 일별 시간대별 승하차인원 정보
'''
import pandas as pd
import numpy as np

df = pd.read_csv('./data/서울교통공사_역별 일별 시간대별 승하차인원 정보_20221231.csv')
# print(df)

df_17_19 =  df[['역명','17-18시간대', '18-19시간대']]
df_st = df_17_19.groupby('역명').sum()
df_su = df_st[['17-18시간대', '18-19시간대']].sum(axis=1)
# print(df_su)
print(df_su.idxmax(), df_su.max())

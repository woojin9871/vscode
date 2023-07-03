import pandas as pd
import numpy as np

df = pd.read_csv('./data/서울교통공사_역별 일별 시간대별 승하차인원 정보_20221231.csv')
# print(df)

# df_on =  df[['역명','승하차구분', '06시이전','06-07시간대','07-08시간대','08-09시간대','09-10시간대','10-11시간대','11-12시간대','12-13시간대','13-14시간대','14-15시간대','15-16시간대','16-17시간대','17-18시간대','18-19시간대','19-20시간대','20-21시간대','21-22시간대','22-23시간대','23-24시간대','24시이후']]
# df_fir = df_on[df_on['승하차구분']=='승차']
# df_st = df_fir.groupby('역명').sum()
# df_su = df_st[['06시이전','06-07시간대','07-08시간대','08-09시간대','09-10시간대','10-11시간대','11-12시간대','12-13시간대','13-14시간대','14-15시간대','15-16시간대','16-17시간대','17-18시간대','18-19시간대','19-20시간대','20-21시간대','21-22시간대','22-23시간대','23-24시간대','24시이후']].sum(axis=1)
# # df_su = df.iloc[: ,6:]
# sort = df_su.sort_values()

# print(sort.tail(10))


# 선생님
df_brd = df[df['승하차구분']=='승차']
# print(df_brd.shape[0])

df_brd = df_brd.loc[:, df_brd.columns != '고유역번호(외부역코드)']
df_brd = df_brd.loc[:, df_brd.columns != '연번']
print(df_brd.columns)

# print(df_brd.groupby('호선', '역명').sum())    # 상하로 합계

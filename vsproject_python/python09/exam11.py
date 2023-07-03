'''
    .data/서울시 지하철 호선별 역별 시간대별 승하차 인원 정보.csv
            2022년 데이터만 사용해서
            출근 시간   (7시 ~ 9시) 시간3대에
                        가장 혼잡한 역을 찾아보시오
'''
import numpy as np
import pandas as pd

df_tra = pd.read_csv('./data/서울시 지하철 호선별 역별 시간대별 승하차 인원 정보2.csv')
# print(df_tra)

# df_tra_t = df_tra.melt(id_vars=['07시-08시 승차인원', '08시-09시 승차인원' ])
# print(df_tra_t)

df_tra_m = df_tra[['사용월']]
# print(df_tra_m)
# print(df_tra_m.shape[0])

df2 = df_tra_m[df_tra_m['사용월']==202201]
print(df2)
print(df2.shape[0])









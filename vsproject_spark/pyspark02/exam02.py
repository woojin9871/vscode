'''
    서울시 기간별 대기환경
    2020년 구별 초미세먼지 평균을 구하시오
'''
import pandas as pd
import numpy as np

df1 = pd.read_csv('./data/서울시_기간별_시간평균_대기환경_정보_2020.01.csv')
df2 = pd.read_csv('./data/서울시_기간별_시간평균_대기환경_정보_2020.02.csv')
df3 = pd.read_csv('./data/서울시_기간별_시간평균_대기환경_정보_2020.03.csv')
df4 = pd.read_csv('./data/서울시_기간별_시간평균_대기환경_정보_2020.04.csv')

df_tot = pd.concat([df1, df2, df3, df4])
print(df_tot)

print(df_tot[['측정소명', '초미세먼지(㎍/㎥)']])



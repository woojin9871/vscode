'''
    .data/period.xlsx   서울 대시 정보      2023년 1월 ~ 2월
            구별로 구분해서
                        각 구의     미세먼지 평균   미세먼지 분산   
                                    초미세먼지 평균 초미세먼지 분산
                        영등포 얼마
'''
import numpy as np
import pandas as pd

df = pd.read_excel('./data/period.xlsx')
df_v = df[['측정소명', '미세먼지', '초미세먼지']]
print(df_v)


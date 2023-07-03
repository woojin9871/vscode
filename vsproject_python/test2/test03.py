'''
    한국교통안정공단 자동차 결함 데이터를 분석하여
    https://www.data.go.kr/data/3048950/fileData.do
    제조사별로 리콜수를 출력하시오
'''
import pandas as pd
import numpy as np

# df = pd.read_csv('./data/한국교통안전공단_자동차결함 리콜현황_20211231.csv')
# # print(df)

# df_my = df[['제작자', '리콜사유']]
# print(df_my.groupby('제작자').count().sort_values(by=['리콜사유'], axis=0))

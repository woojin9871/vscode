'''
    ./data/2020_0918_company_list.csv
                상장일
                                    연도    월      일
                        2020-05-09
'''                     
import numpy as np
import pandas as pd

df_com = pd.read_csv('./data/2020_0918_company_list.csv', low_memory=False) # 결측값 다수 있음
# print(df_com)

df_com_v = df_com.iloc[:, [4]]
# print(df_com_v)

com_split = df_com_v.상장일.str.split('-')
print(com_split)

year = com_split.str.get(0)
month = com_split.str.get(1)
day = com_split.str.get(2)
# print(year)
# print(month)
# print(day)
df_com['Year'] = year
df_com['Month'] = month
df_com['Day'] = day

print(df_com[['회사명', '종목코드', 'Year', 'Month', 'Day']])

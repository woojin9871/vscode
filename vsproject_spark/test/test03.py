import pandas as pd
import numpy as np

df = pd.read_csv('./data/한국교통안전공단_자동차결함 리콜현황_20211231.csv')
# print(df)

df_my = df[['제작자', '리콜사유']]
df_ri = df_my[df_my['리콜사유'].str.contains('브레이크')]
df_ri2 = df_my[df_my['리콜사유'].str.contains('엔진오일')]
df_tot = pd.concat([df_ri, df_ri2])
# print(df_tot)
df_cr = df_tot.groupby('제작자').count().sort_values(by=['리콜사유'], axis=0)
print(df_cr)



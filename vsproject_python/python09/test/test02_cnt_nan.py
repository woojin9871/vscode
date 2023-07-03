import numpy as np
import pandas as pd

df = pd.read_csv('./data/country_timeseries.csv')
# print(df.head(n=5))
# print(df.shape[0])
# print(df['Cases_Guinea'].count())   # 값이 있어야 카운트
# print(df.shape[0]-df['Cases_Guinea'].count())

print(df['Deaths_Guinea'].count)
print(df.shape[0]-df['Deaths_Guinea'].count())

# 다른 방법
print(df.isnull().head(n=5))
print(np.count_nonzero( df['Deaths_Guinea'].isnull()))

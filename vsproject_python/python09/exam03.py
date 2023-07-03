'''
    ./data/california-history.csv
            전체 행 갯수를 구하시오
            hospitalizedCurrently 컬럼에서 결측갯수를 출력하시오
            결측값은 모두 0으로 바꾸시오
'''

import numpy as np
import pandas as pd

df = pd.read_csv('./data/california-history.csv')

print(df.head(n=10), '\n')
# print(df.fillna(0).head(n=10))
# print(df.fillna(method='ffill').head(n=10))

total_row = df.shape[0]
print(total_row)
print(df['Cases_Liberia'].fillna(method='ffill').count())

# print(df['hospitalizedCurrently'].count())
# print(df.shape[0]-df['hospitalizedCurrently'].count())

# print(df.fillna('0'))
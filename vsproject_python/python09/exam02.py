'''
    ./data/country_timeseries.csv
            결측값이 많음
            결측값을 모두 0으로 바꾸시오
            결측값을 method-ffill 사용해서 바꾸시오
'''

import numpy as np
import pandas as pd

df = pd.read_csv('./data/country_timeseries.csv')

print(df.fillna('0'))
# print(df.fillna(method='ffill'))



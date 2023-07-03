'''
    fruit   date        price
    바나나  2018.1.1    3500
    바나나  2019.4.1    3100
    바나나  2020.7.1    4000
    사과    2018.1.1    5500
    사과    2019.4.1    7500
    사과    2020.7.1    6500
    딸기    2018.1.1    12000
    딸기    2019.4.1    11000
    딸기    2020.7.1    13000

            date_dt 변경
            연도별로 평균 구하시오
            그래프를 그리시오
'''
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt 

data = { 'fruit' : ['바나나', '바나나', '바나나', '사과', '사과', '사과', '딸기', '딸기', '딸기'],
         'date' : ['2018.1.1', '2019.4.1', '2020.7.1', '2018.1.1', '2019.4.1', '2020.7.1', '2018.1.1', '2019.4.1', '2020.7.1'],
         'price' : [3500, 3100, 4000, 5500, 7500, 6500, 12000, 11000, 13000]}
df_data = pd.DataFrame(data)
# print(df_data)

df_data['date_dt'] = pd.to_datetime(df_data['date'])
# print(df_data) 

df_data['date_dt'] = df_data['date_dt'].dt.year
# print(df_data)

df_data_y = df_data.groupby(['date_dt', 'price']).size()
print(df_data_y)


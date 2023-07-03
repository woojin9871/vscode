import numpy as np
import pandas as pd

df_ebo = pd.read_csv('./data/country_timeseries.csv', low_memory=False)
# print(df_ebo)
print(df_ebo.shape[0])

df_ebo_v = df_ebo.iloc[:, [0, 1, 2, 3, 10, 11]]   # 행 전부, 0, 1번째
# print(df_ebo_v)

df_ebo_long = df_ebo.melt(id_vars=['Date', 'Day'])
# print(df_ebo_long)

var_split = df_ebo_long.variable.str.split('_')
# print(type(var_split))    # Series
# print(type(var_split[0])) # list

status = var_split.str.get(0)
country = var_split.str.get(1)
print(df_ebo_long)

df_ebo_long['status'] = status
print(df_ebo_long)




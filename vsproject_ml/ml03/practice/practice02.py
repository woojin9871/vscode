import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt 

df_bank = pd.read_csv('./data/banklist.csv', parse_dates=['Closing Date', "Updated Date"])
# print(df_bank.info())
df_bank['close_year'] = df_bank['Closing Date'].dt.year     # str.contains('문자열')
# print(df_bank.head(n=10))

# 분기 quarter
df_bank['close_year'], df_bank['close_q'] = df_bank['Closing Date'].dt.year, df_bank['Closing Date'].dt.quarter
# print(df_bank[['Closing Date', 'close_year', 'close_q']])
df_bank_y = df_bank.groupby(['close_year']).size()
print(df_bank_y)
# print(df_bank.groupby(['close_year', 'close_q']).size())

# fig = plt.figure()
sub = plt.subplot()
sub = df_bank_y.plot()
plt.show()
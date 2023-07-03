import numpy as np
import pandas as pd

data = {'A' : [2, 4, np.NaN, 8, 10, 12, 14, 16, 18, 20],
        'B' : [1, 3, 5, np.NaN, 9, 11, 13, 15, 17, 19],
        'C' : [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]}
df = pd.DataFrame(data)
print(df, '\n')
# print(df.fillna(method='ffill'))
# print(df.fillna(method='bfill'))
# print(df.interpolate())
print(df.dropna(axis=1))



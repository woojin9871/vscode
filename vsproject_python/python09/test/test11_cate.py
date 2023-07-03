import pandas as pd
import numpy as np

emp = {
    'id' : ['1001', '1002', '1003', '1004', '1005'],
    'gender' : ['m', 'm', 'f', 'm', 'f'],
    'salery' : [10000, 20000, 50000, 30000, 40000]
}
df = pd.DataFrame(emp)
print(df.info())
df2 = df
df2 = df['gender'].astype('category')
print(df2.info())

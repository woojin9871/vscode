import pandas as pd
import numpy as np
import glob as glob

sample_data = {
    'id' : [1000, 1001, 1002, 1004],
    'job' : ['manager', 'devloper', 'manager', 'designer'],
    'salery' : [5000, 3000, 6000, 10000]
}

df = pd.DataFrame(sample_data)
print(df)
# print(df['job'].str.capitalize())

# print(df['job'].str.replace('manger', 'marketer'))

# print(df['phn1_phn2'].str.split('-'))
split_1 = df['phn1_phn2'].str.split('-').str.get(0)
df['phn1'] = split_1
print(df)

import numpy as np
import pandas as pd

# dict
data = {'A' : ['kim', 'park', 'choi', 'lee'],
        'B' : ['abcc', 'pppp', 'cccc', 'rrrr'],
        'math' : ['A', 'B', 'C', 'B'],
        'scholar' : [100, 200, 300, 400]}
# dataframe
df = pd.DataFrame(data)
print(df, '\n')

# print(df.melt(id_vars='A', value_vars='B'))   # variable, value
print(df.melt(id_vars=['A', 'B'], value_vars=['math', 'scholar'],
              var_name='subject', value_name='grade').sort_values(by='A'))


